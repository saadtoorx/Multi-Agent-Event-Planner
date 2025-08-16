from crewai import Task
from tools import agent_tools
from pydantic import BaseModel

# Define VenueDetails model here since it's used in tasks
class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

def agent_tasks(venue_coordinator, logistic_manager, marketing_communications_agent):

    #Task 1: Venue Task
    venue_task = Task(
        description = "Find a venue in {event_city} that meets criteria for {event_topic}",
        
        expected_output= "All the details of the specifically chosen venue you found to accommodate the event",
        
        human_input= True,

        #Outputs the venue details in a JSON format which is utilized and formatted using Pydantic (VenueDetails)
        output_json= VenueDetails,
        output_file= "venue_details.json",

        agent = venue_coordinator
    )

    #Task 2: Logistics Task

    logistics_task = Task(
        description= "Coordinate catering and equipment for an event with {expected_participants} participants on {tentative_date}.",
        
        expected_output= "Confirmations of all logistics arrangements including catering, equipment rental, and setup details.",
        human_input= True,

        # #Async Execution: This task will be executed along with the other tasks as parallel execution 
        # async_execution= True,
        context= [venue_task],

        agent = logistic_manager
    )

    #Task 3: Marketing Task

    marketing_task = Task(
        description = "Promote the {event_topic} aiming to engage at least {expected_participants} potential attendees.",

        expected_output= "A comprehensive report on marketing activities and attendee engagement formatted as markdown.",

        human_input= True,
        # async_execution= True,
        context= [venue_task, logistics_task],
        output_file= "marketing_report.md",

        agent = marketing_communications_agent
    )

    return venue_task, logistics_task, marketing_task
