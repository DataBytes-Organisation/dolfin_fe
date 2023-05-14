import dash_html_components as html
import dash_core_components as dcc

from layout.sidebar.sidebar import sidebar
from layout.navbar.navbar import navbar, logo
#from components.footer import Footer  # Import the Footer component

content = html.Div(id="page-content", className="content-container")

# Define the chatbox component with unique IDs
chatbox = html.Div(
    [
        html.Button(
            "Chat with me!",
            id="chat-button-unique",
            className="chat-button"
        ),
        html.Div(
            id="chat-container-unique",
            className="chat-container",
            children=[
                html.Div(
                    id="chat-messages-unique",
                    className="chat-messages"
                ),
                dcc.Input(
                    id="chat-input-unique",
                    className="chat-input",
                    placeholder="Type your message..."
                ),
            ],
        ),
    ],
    className="chat-wrapper"
)

# Wrap the content, sidebar, chatbox, and footer inside a new div with the "page-container" class
page_container = html.Div(
    [
        sidebar,
        content,
        chatbox,  # Added the chatbox component
        
        #Footer(),  # Add the Footer component
    ],
    className="page-container",
)

# Define the top-level layout with chatbox included
layout = html.Div([dcc.Location(id="url"), navbar, logo, page_container])
