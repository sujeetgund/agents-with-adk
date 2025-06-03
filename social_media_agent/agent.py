from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.callback_context import CallbackContext
from .sub_agents.linkedin_agent import linkedin_agent


def set_initial_state(callback_context: CallbackContext):
    if not callback_context.state.get("user:name"):
        callback_context.state["user:name"] = "Sujeet Gund"


root_agent = Agent(
    name="social_media_agent",
    model="gemini-2.0-flash",
    description="Social Media Agent for writing posts across various platforms.",
    sub_agents=[linkedin_agent],
    instruction="""
    You are a Social Media Agent designed to assist user with writing posts across various platforms including LinkedIn, Twitter, and Facebook.
    
    USER INFORMATION:
    - Name: {{user:name}}
    
    GUIDELINES:
    - Always ask the user for the platform they want to post on.
    - If the user specifies a platform, use the corresponding sub-agent to generate the post.
    - If the user does not specify a platform, use LinkedIn as the default platform.
    """,
    before_agent_callback=set_initial_state,
)
