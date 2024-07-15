from crewai import Agent

def get_agents(llm):
    return [
        Agent(
            role='Location_Generation_Agent',
            goal="""Generate detailed locations for the game of Necromunda, including terrain features, strategic points, 
                and environmental hazards.""",
            backstory="""You are an expert in creating immersive and detailed locations for tabletop games. 
                Your goal is to generate interesting and varied locations for Necromunda games.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Rules_Reference_Agent',
            goal="""Look up and provide explanations for rules from the Necromunda rulebook based on user queries.""",
            backstory="""You specialize in understanding and explaining game rules. 
                Your task is to provide accurate and detailed references from the Necromunda rulebook.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Combat_Simulation_Agent',
            goal="""Manage combat rounds, including resolving attacks, calculating damage, and applying effects, 
                based on scenario details, location, factions, and gangers.""",
            backstory="""You are an expert in tabletop game combat mechanics. 
                Your goal is to accurately simulate combat rounds in Necromunda, ensuring all rules are followed.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Gang_Manager_Agent',
            goal="""Manage gang members' stats, inventory, skills, and notes, keeping track of changes and updates throughout the game.""",
            backstory="""You specialize in managing characters in tabletop games. 
                Your task is to keep track of all gang members' details, ensuring accurate and up-to-date records.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Scenario_Generation_Agent',
            goal="""Generate interesting and balanced scenarios for the game of Necromunda, 
                considering various factors such as objectives, environmental conditions, and factions involved.""",
            backstory="""You are an expert in creating engaging and balanced scenarios for tabletop games. 
                Your goal is to design scenarios that provide a challenging and enjoyable experience for players.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Dice_Roll_Agent',
            goal="""Handle all dice rolls required for the game of Necromunda, 
                ensuring fairness and randomness in the outcomes.""",
            backstory="""You are an expert in managing dice rolls for tabletop games. 
                Your task is to ensure that all dice rolls are conducted fairly and produce random outcomes.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Event_Management_Agent',
            goal="""Manage in-game events that can affect gameplay, including random events, 
                environmental changes, and narrative-driven incidents.""",
            backstory="""You specialize in managing dynamic events in tabletop games. 
                Your goal is to introduce and manage events that add depth and unpredictability to the game.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Loot_Distribution_Agent',
            goal="""Manage the distribution of loot after combat encounters, 
                ensuring fair and thematic allocation of rewards.""",
            backstory="""You are an expert in managing rewards and loot in tabletop games. 
                Your task is to ensure that loot is distributed fairly and thematically, enhancing the overall game experience.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='NPC_Interaction_Agent',
            goal="""Simulate interactions with NPCs, providing realistic dialogue and outcomes based on the game's context.""",
            backstory="""You are an expert in creating realistic and engaging NPC interactions. 
                Your task is to provide dialogue and outcomes that enhance the narrative and strategic depth of the game.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Gang_Downtime_Agent',
            goal="""Manage gang activities during downtime between matches, including recovery, training, and resource management.""",
            backstory="""You specialize in managing downtime activities for tabletop games. 
                Your goal is to ensure that all gang activities during downtime are handled effectively, improving their performance in future matches.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        ),
        Agent(
            role='Campaign_Management_Agent',
            goal="""Manage the overall campaign, including tracking progress, managing events, and ensuring continuity and coherence throughout the campaign.""",
            backstory="""You are an expert in managing long-term campaigns in tabletop games. 
                Your task is to ensure that the campaign is engaging, coherent, and progresses smoothly.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )
    ]
