import os
import pandas as pd
from crewai import Task, Crew
from crewai_tools import FileReadTool, DirectoryReadTool

from langchain_groq import ChatGroq
from agents import get_agents
from tasks import get_tasks  # Import the get_tasks function


def main():
    model = 'llama3-70b-8192'

    llm = ChatGroq(
        temperature=0, 
        groq_api_key=os.getenv('GROQ_API_KEY'), 
        model_name=model
    )

    print('Necromunda Game Assistant')
    multiline_text = """
    The Necromunda Game Assistant is designed to guide players through various aspects of the Necromunda game. 
    It leverages a team of AI agents, each with a specific role, to generate locations, manage gangs, simulate combat, 
    and provide rules references. Whether you're a seasoned player or a beginner, this application provides valuable 
    assistance in managing your Necromunda game.
    """

    print(multiline_text)

    agents = get_agents(llm)

    user_action = input("Select an action (generate location, look up rules, simulate combat, manage gang, generate scenario, roll dice, manage event, distribute loot, NPC interaction, gang downtime, manage campaign): ")
    data_upload = False

    # Check if there is a .csv file in the current directory
    if any(file.endswith(".csv") for file in os.listdir()):
        sample_fp = [file for file in os.listdir() if file.endswith(".csv")][0]
        try:
            # Attempt to read the uploaded file as a DataFrame
            df = pd.read_csv(sample_fp).head(5)

            # If successful, set 'data_upload' to True
            data_upload = True

            # Display the DataFrame in the app
            print("Data successfully uploaded and read as DataFrame:")
            print(df)
        except Exception as e:
            print(f"Error reading the file: {e}")

    tasks = get_tasks(user_action, data_upload, df if data_upload else None, agents)

    if tasks:
        crew = Crew(agents=agents, tasks=tasks, verbose=True)
        result = crew.kickoff()

        print(result)

        with open('necromunda_output.md', "a") as file:
            print('\n\nThese results have been exported to necromunda_output.md')
            file.write(result)
    else:
        print("Invalid action selected or no tasks defined.")

if __name__ == "__main__":
    main()
