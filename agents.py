from crewai import Agent

from tools import agent_tools

search_tool, scrape_tool = agent_tools()

def create_agents():

    #Agent 1: Venue Coordinator
    venue_coordinator = Agent(
        role = "Venue Coordinator",
        goal = "Identify and book and appropriate venue based on the event requirements",
        
        tools = [search_tool, scrape_tool],
        verbose = True,
        
        backstory = (
            "With a keen search of space and understanding of event logistics, you excel at finding and securing the perfect venue that fits the event's theme, size and budget constrains."
        )
    )

    #Agent 2: Logistic Manager
    logistic_manager = Agent(
        role = 'Logistic Manager',
        goal = (
            "Manage all the logistics for the event, including catering and equipment"
        ),
        
        tools = [search_tool, scrape_tool],
        verbose = True,
        
        backstory = (
            "Organized and detail-oriented, you ensure that every logistical aspect of the event from catering to equipment setup is flawlessly executed to create a seamless experience for all attendees."
        )
    )

    #Agent 3: Marketing and Communications Agent
    marketing_communications_agent = Agent(
        role = 'Marketing and Communications Agent',
        goal = "Effectively market the event and communicate with the participants.",
        
        tools = [search_tool, scrape_tool],
        verbose = True,
        
        backstory = (
            "Creative and communicative, you craft compelling messages and engage with potential attendees across various channels, ensuring maximum event exposure and participation."
        )
    )

    return venue_coordinator, logistic_manager, marketing_communications_agent