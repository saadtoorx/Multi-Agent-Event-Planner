import streamlit as st
import warnings
import os
import json
from datetime import datetime
from pydantic import BaseModel

# Suppress warnings
warnings.filterwarnings("ignore")

# Configure page
st.set_page_config(
    page_title="Multi-Agent Event Planner",
    page_icon="🗓️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'api_keys_configured' not in st.session_state:
    st.session_state.api_keys_configured = False
if 'crew_result' not in st.session_state:
    st.session_state.crew_result = None
if 'event_details' not in st.session_state:
    st.session_state.event_details = {}
if 'planning_started' not in st.session_state:
    st.session_state.planning_started = False

# Define VenueDetails model
class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

def configure_api_keys():
    with st.sidebar:
        with st.expander("🔑 API Configuration", expanded=False):
            st.header("⚙️ Configuration")
            st.markdown("---")
            st.markdown("🔑 API Configuration")
            st.markdown("Please enter your API keys to begin:")
        
            openai_api_key = st.text_input("OpenAI API Key", type="password", key="openai_key")
            serper_api_key = st.text_input("Serper API Key", type="password", key="serper_key")
        
            if st.button("Configure Keys", type="primary"):
                if openai_api_key and serper_api_key:
                    # Set environment variables
                    os.environ["OPENAI_API_KEY"] = openai_api_key
                    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
                    os.environ["SERPER_API_KEY"] = serper_api_key
                    
                    st.session_state.api_keys_configured = True
                    st.success("✅ API Keys configured successfully!")
                    st.rerun()
                else:
                    st.error("❌ Please enter both API keys.")
    
    return openai_api_key and serper_api_key

def main_interface():
    col1h, col2h, col3h = st.columns([1, 6, 1])

    with col2h:
        # Center and style the title using HTML/CSS
        st.markdown(
            """
            <h1 style='text-align: center; font-size: 3em; font-family: "Montserrat", Arial, sans-serif;'>
                🗓️ Multi-Agent Event Planner
            </h1>
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
            h1 {
                font-family: 'Montserrat', Arial, sans-serif !important;
            }
            </style>
            """,
            unsafe_allow_html=True
            )

        st.markdown(
            """
            <h2 style='text-align: center; font-size: 1em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: -20px;'>
                AI-powered agents collaborating to plan, coordinate, and market your events seamlessly
            </h2>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    cola1, cola2, cola3, cola4, cola5 = st.columns([2, 4, 1, 3, 2])

    with cola2:
        event_topic = st.text_input(
            "Event Topic", 
            value="Tech Innovation Conference",
            help="The main topic or theme of your event"
        )
        event_city = st.text_input(
            "Event City", 
            value="San Francisco",
            help="The city where the event will be held"
        )    
        tentative_date = st.date_input(
            "Tentative Date",
            value=datetime(2025, 11, 15),
            help="Preferred date for the event"
        )
        event_description = st.text_area(
            "Event Description",
            value="A gathering of tech innovators and industry leaders to explore the latest trends and advancements in technologies.",
            help="Detailed description of your event"
        )
        expected_participants = st.number_input(
            "Expected Participants",
            min_value=1,
            value=500,
            help="Number of people expected to attend"
        )
        budget = st.number_input(
            "Budget ($)",
            min_value=0,
            value=20000,
            help="Total budget for the event"
        )
        venue_type = st.selectbox(
            "Venue Type",
            ["Conference Center", "Hotel", "Convention Center", "University", "Other"],
            help="Type of venue preferred for the event"
        )
    
    with cola4:
        # Store event details in session state
        st.session_state.event_details = {
            'event_topic': event_topic,
            'event_description': event_description,
            'event_city': event_city,
            'tentative_date': tentative_date.strftime("%Y-%m-%d"),
            'expected_participants': expected_participants,
            'budget': budget,
            'venue_type': venue_type
        }


        # Display event summary
        st.subheader("📋 Event Summary")
        with st.expander("View Event Details", expanded=False):
            st.json(st.session_state.event_details)

        cola4_1, cola4_2 = st.columns([1, 1])

        with cola4_1:
            if st.button("🚀 Start Planning", type="primary", disabled=not st.session_state.api_keys_configured):
                if not st.session_state.api_keys_configured:
                    st.error("❌ Please configure your API keys in the sidebar first.")
                else:
                    st.session_state.planning_started = True
                    st.rerun()
        
        with cola4_2:
            if st.button("🔄 Reset Application"):
                for key in ['planning_started', 'crew_result', 'event_details']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
    
    st.markdown("---")
    st.markdown(
            """
            <h6 style='text-align: center; font-size: 0.8em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: 2px;'>
                Developed & Designed by saadtoorx
            </h6>
            <h6 style='text-align: center; font-size: 0.8em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: 2px;'>
                GitHub: @saadtoorx | LinkedIn: @saadtoorx  | X: @saadtoorx
            </h6>
            """,
            unsafe_allow_html=True
        )

def execute_event_planning():

    col1h, col2h, col3h = st.columns([1, 6, 1])

    with col2h:
        # Center and style the title using HTML/CSS
        st.markdown(
            """
            <h1 style='text-align: center; font-size: 3em; font-family: "Montserrat", Arial, sans-serif;'>
                🗓️ Multi-Agent Event Planner
            </h1>
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
            h1 {
                font-family: 'Montserrat', Arial, sans-serif !important;
            }
            </style>
            """,
            unsafe_allow_html=True
            )

        st.markdown(
            """
            <h2 style='text-align: center; font-size: 1em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: -20px;'>
                AI-powered agents collaborating to plan, coordinate, and market your events seamlessly
            </h2>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.header("🎯 Event Planning Execution")
    st.markdown("This section executes the event planning process using AI agents.")
    
    # Show event details being processed
    with st.expander("📋 Event Being Planned", expanded=True):
        st.json(st.session_state.event_details)
    
    # Option to use real CrewAI agents
    use_real_agents = st.checkbox("🤖 Use Real CrewAI Agents (requires proper setup)", value=False)
    
    # Execute button
    if st.button("🚀 Execute Planning", type="primary"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            if use_real_agents:
                # Try to use real CrewAI agents
                status_text.text("🤖 Initializing CrewAI agents...")
                progress_bar.progress(0.1)
                result = execute_with_crewai()
                st.session_state.crew_result = result
            else:
                # Use simulated execution
                status_text.text("🏢 Processing venue coordination...")
                progress_bar.progress(0.3)
                
                status_text.text("📦 Handling logistics arrangements...")
                progress_bar.progress(0.6)
                
                status_text.text("📢 Developing marketing strategy...")
                progress_bar.progress(0.9)
            
            # Show final result
            progress_bar.progress(1.0)
            status_text.text("✅ Event planning completed successfully!")
            
            # Show results
            display_results()
            
        except Exception as e:
            st.error(f"❌ Error during execution: {str(e)}")
            st.error("Falling back to simulated results...")
            display_results()
    
    st.markdown("---")
    st.markdown(
            """
            <h6 style='text-align: center; font-size: 0.8em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: 2px;'>
                Developed & Designed by saadtoorx
            </h6>
            <h6 style='text-align: center; font-size: 0.8em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: 2px;'>
                GitHub: @saadtoorx | LinkedIn: @saadtoorx  | X: @saadtoorx
            </h6>
            """,
            unsafe_allow_html=True
        )

def execute_with_crewai():
    """Execute planning using real CrewAI agents"""
    try:
        from agents import create_agents
        from tasks import agent_tasks
        from crewai import Crew
        
        # Create agents
        venue_coordinator, logistic_manager, marketing_communications_agent = create_agents()
        
        # Create tasks
        venue_task, logistics_task, marketing_task = agent_tasks(
            venue_coordinator, logistic_manager, marketing_communications_agent
        )
        
        # Create and execute crew
        event_management_crew = Crew(
            agents=[venue_coordinator, logistic_manager, marketing_communications_agent],
            tasks=[venue_task, logistics_task, marketing_task],
            verbose=True
        )
        
        # Execute crew
        result = event_management_crew.kickoff(inputs=st.session_state.event_details)
        return result
        
    except Exception as e:
        raise Exception(f"CrewAI execution failed: {str(e)}")

def display_results():

    """Display the planning results"""
    st.success("✅ Event planning completed successfully!")
    
    st.header("📊 Planning Results")
    
    # Show real CrewAI results if available
    if st.session_state.crew_result:
        st.subheader("🤖 CrewAI Agent Results")
        with st.expander("📄 Complete Agent Report", expanded=True):
            if hasattr(st.session_state.crew_result, 'raw'):
                st.markdown(st.session_state.crew_result.raw)
            else:
                st.text(str(st.session_state.crew_result))
    
    # Create simulated results based on inputs
    venue_result = {
        "name": f"{st.session_state.event_details['event_city']} Convention Center",
        "address": f"123 Event Street, {st.session_state.event_details['event_city']}",
        "capacity": st.session_state.event_details['expected_participants'] + 50,
        "booking_status": "Available"
    }
    
    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏢 Venue Details")
        st.json(venue_result)
        
        # Download venue details
        st.download_button(
            label="📄 Download Venue Details",
            data=json.dumps(venue_result, indent=2),
            file_name="venue_details.json",
            mime="application/json"
        )
    
    with col2:
        st.subheader("📢 Marketing Report")
        marketing_report = f"""# Marketing Strategy Report

        ## Event Overview
        - **Event**: {st.session_state.event_details['event_topic']}
        - **Location**: {st.session_state.event_details['event_city']}
        - **Date**: {st.session_state.event_details['tentative_date']}
        - **Expected Attendees**: {st.session_state.event_details['expected_participants']}

        """
                
        st.markdown(marketing_report)
        
        # Download marketing report
        st.download_button(
            label="📄 Download Marketing Report",
            data=marketing_report,
            file_name="marketing_report.md",
            mime="text/markdown"
        )
    
    # Check for generated files from CrewAI
    if st.session_state.crew_result:
        st.subheader("📁 Generated Files")
        
        # Check for venue details JSON file
        try:
            if os.path.exists("venue_details.json"):
                with open("venue_details.json", "r") as f:
                    real_venue_data = json.load(f)
                st.success("✅ Real venue details file generated!")
                with st.expander("🏢 CrewAI Venue Details"):
                    st.json(real_venue_data)
        except:
            pass
        
        # Check for marketing report file
        try:
            if os.path.exists("marketing_report.md"):
                with open("marketing_report.md", "r") as f:
                    real_marketing_data = f.read()
                st.success("✅ Real marketing report file generated!")
                with st.expander("📢 CrewAI Marketing Report"):
                    st.markdown(real_marketing_data)
        except:
            pass
    
    # Complete summary download
    summary_report = f"""# Complete Event Planning Summary

## Event Details
{json.dumps(st.session_state.event_details, indent=2)}

## Results
{marketing_report}

## Venue Details
{json.dumps(venue_result, indent=2)}

## CrewAI Results
{str(st.session_state.crew_result) if st.session_state.crew_result else "No CrewAI results available"}
"""
    
    st.download_button(
        label="📄 Download Complete Summary",
        data=summary_report,
        file_name="event_planning_summary.md",
        mime="text/markdown"
    )
    
    # Reset for new planning
    if st.button("🔄 Start New Planning"):
        for key in ['planning_started', 'crew_result']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

def main():
    """Main application function"""
    
    # Sidebar for API configuration
    
    configure_api_keys()
    
    if st.session_state.api_keys_configured:

        with st.sidebar:

            st.success("✅ API Keys Configured")
            st.markdown("---")
            st.markdown("### 🎯 Planning Status")
            
            if st.session_state.planning_started:
                st.info("🚀 Planning in progress...")
            else:
                st.info("⏳ Ready to start planning")
            
            # Reset button
            st.markdown("---")

            with st.expander("ℹ️ Application Info"):
                st.markdown("""
                ### ℹ️ Application Info

                **Agents:**
                - **🏢 Venue Coordinator**: Identifies, evaluates, and books suitable venues for your event.
                - **📦 Logistics Manager**: Manages catering, equipment, transportation, and event setup logistics.
                - **📢 Marketing Agent**: Designs and executes marketing strategies to maximize event reach and engagement.

                **Tasks:**
                - **Venue Selection & Booking**: Researches venues, checks availability, and secures bookings.
                - **Logistics Planning**: Arranges catering, equipment, and coordinates on-site logistics.
                - **Marketing Strategy Development**: Plans campaigns, creates promotional content, and manages outreach.

                **Tools:**
                - **SerperDev Tool**: Enables web search and data gathering for venue and logistics research.
                - **Scrape Website Tool**: Extracts detailed information from websites for planning and coordination.
                - **OpenAI API**: Powers agent intelligence and natural language capabilities.
                - **CrewAI Framework**: Orchestrates multi-agent collaboration and task execution.
                """)
    
    # Main interface
    if st.session_state.api_keys_configured:
        if st.session_state.planning_started:
            execute_event_planning()
        else:
            main_interface()
    else:
        # Centered layout using columns
        col_left, col_center, col_right = st.columns([1, 7, 1])
        with col_center:
            col1h, col2h, col3h = st.columns([1, 6, 1])

            with col2h:
                # Center and style the title using HTML/CSS
                st.markdown(
                    """
                    <h1 style='text-align: center; font-size: 3em; font-family: "Montserrat", Arial, sans-serif;'>
                        🗓️ Multi-Agent Event Planner
                    </h1>
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
                    h1 {
                        font-family: 'Montserrat', Arial, sans-serif !important;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <h2 style='text-align: center; font-size: 1em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: -20px;'>
                        AI-powered agents collaborating to plan, coordinate, and market your events seamlessly
                    </h2>
                    """,
                    unsafe_allow_html=True
                )
            

            st.markdown("---")

            col1, col2, col3 = st.columns([3, 1,3])
            with col1:
                st.info("👈 Please configure your API keys in the sidebar to get started.")

                # Show demo information
                st.markdown("""
                ## 🤖 About This Application

                This Multi-Agent Event Planner uses AI agents to help you plan events efficiently:

                - **🏢 Venue Coordinator**: Finds and books appropriate venues
                - **📦 Logistics Manager**: Handles catering, equipment, and setup
                - **📢 Marketing Agent**: Creates marketing strategies and materials
                            
                ### 📝 Sample Event Ideas
                - **Tech Conference**: Innovation summit in San Francisco for 500 participants
                - **Green Energy Expo**: Renewable energy showcase in Seattle for 600 participants
                - **Art Festival**: Cultural celebration in Austin for 800 participants
                - **Healthcare Symposium**: Medical advancements forum in Boston for 400 participants

                """)
            
            with col3:
                st.image("images/png_start.png", width=400, )  # Set width in pixels (e.g., 300)
                st.markdown("""
                       ### 🚀 Getting Started
                    1. Enter your OpenAI and Serper API keys in the sidebar
                    2. Fill out your event details
                    3. Click "Start Event Planning" to begin the process
                    4. Choose between simulated or real AI agent execution
                    5. Download your complete event plan     

                """)
            
            st.markdown("---")
            st.markdown(
                    """
                    <h6 style='text-align: center; font-size: 0.8em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: 2px;'>
                        Developed & Designed by saadtoorx
                    </h6>
                    <h6 style='text-align: center; font-size: 0.8em; font-family: "Montserrat", Arial, sans-serif; color: #555; margin-top: 2px;'>
                        GitHub: @saadtoorx | LinkedIn: @saadtoorx  | X: @saadtoorx
                    </h6>
                    """,
                    unsafe_allow_html=True
                )



if __name__ == "__main__":
    main()

