from uuid import uuid4
import os
from aws_cdk import (
    Stack,
    aws_elasticbeanstalk as elasticbeanstalk,
    aws_elasticloadbalancingv2 as elb2,
    aws_route53,
    aws_ec2,
    aws_route53_targets as targets,
    aws_s3_assets,
    aws_s3 as s3
)
from constructs import Construct

class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stage = "PROD"
        self.name = "DolfinFrontEnd"
        self.domain_name = "dolfintechnology.com"
        self.hosted_zone_id = "Z034086312CTYRFF6XA1M"
        self.ssl_certificate_arn = "arn:aws:acm:ap-southeast-2:909874321825:certificate/7284913e-4843-4d30-88e7-d0b55f7ecb4f"

        source_location = aws_s3_assets.Asset(self, f"{self.name}SourceZip",
            path=os.path.join(os.getcwd(), 'app.zip'),
        )

        vpc = aws_ec2.Vpc.from_lookup(self, "VPC", is_default=True) # vpc_id=xyz can be used here if not want to use default vpc

        #app_load_balancer = elb2.ApplicationLoadBalancer(self, f"{self.name}CfnLoadBalancer", vpc=vpc, internet_facing=True)

        # ssl_certificate = elb2.ListenerCertificate.from_arn(self.ssl_certificate_arn)

        # secure_listener = elb2.ApplicationListener(self, f"{self.name}Applistener",
        #     load_balancer=app_load_balancer,
        #     certificates=[ssl_certificate],
        #     default_action=elb2.ListenerAction.fixed_response(status_code=200, content_type='text/plain', message_body='OK'),
        #     port=443,
        #     open=True
        # )

        cfn_application = elasticbeanstalk.CfnApplication(self, f"{self.name}CfnApplication{stage}",
            application_name=f"{self.name}-{uuid4()}",
            description=f"{self.name} description",
            resource_lifecycle_config=None
        )

        source_bundle_property = elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty(
            s3_bucket=source_location.s3_bucket_name,
            s3_key=source_location.s3_object_key
        )

        app_version = elasticbeanstalk.CfnApplicationVersion(self, f"{self.name}AppVersion{stage}",
            application_name=cfn_application.application_name,
            source_bundle= source_bundle_property
        )

        hosted_zone = aws_route53.HostedZone.from_lookup(self, f"{self.name}HostedZone",
            domain_name=self.domain_name    
        )

        cfn_environment = elasticbeanstalk.CfnEnvironment(self, f"{self.name}CfnEnvironment{stage}",
            application_name=cfn_application.application_name,

            # the properties below are optional
            cname_prefix=f"{self.name}cname",
            description="description",
            environment_name=f"{self.name}environment{stage}",
            # operations_role="operationsRole",
            option_settings=[elasticbeanstalk.CfnEnvironment.OptionSettingProperty(
                
                namespace="aws:autoscaling:launchconfiguration",
                option_name="InstanceType",

                # the properties below are optional
                #resource_name="resourceName",
                value="t3.micro"
            ),
            elasticbeanstalk.CfnEnvironment.OptionSettingProperty(
                
                namespace="aws:autoscaling:launchconfiguration",
                option_name="IamInstanceProfile",

                # the properties below are optional
                #resource_name="resourceName",
                value="aws-elasticbeanstalk-ec2-role"
            )],
            solution_stack_name="64bit Amazon Linux 2 v3.5.1 running Python 3.8",
            tier=elasticbeanstalk.CfnEnvironment.TierProperty(
                name="WebServer",
                type="Standard",
            ),
            version_label=app_version.ref
        )

        elastic_beanstalk_target = aws_route53.RecordTarget.from_alias(targets.ElasticBeanstalkEnvironmentEndpointTarget(
            f"{cfn_environment.cname_prefix}.{self.region}.elasticbeanstalk.com",
            )
        )

        aws_route53.ARecord(self, f"{self.name}AliasRecord",
            zone=hosted_zone,
            target=elastic_beanstalk_target, #cfn_environment.attr_endpoint_url
            #record_name=self.domain_name
        )

        app_version.add_depends_on(cfn_application)
        
