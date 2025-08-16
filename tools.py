# Tools for CrewAI agents with fallback for missing packages
import warnings
warnings.filterwarnings("ignore")


def agent_tools():
    """Return agent tools - real versions if available, mock versions as fallback"""
    try:
        from crewai_tools import ScrapeWebsiteTool, SerperDevTool
        search_tool = SerperDevTool()
        scrape_tool = ScrapeWebsiteTool()
        return search_tool, scrape_tool
    except ImportError:
        # Fallback to mock tools if crewai_tools not available
        search_tool = MockSerperDevTool()
        scrape_tool = MockScrapeWebsiteTool()
        return search_tool, scrape_tool