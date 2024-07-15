from crewai import Task

def get_tasks(user_action, data_upload, df, agents):
    tasks = []

    if user_action == "generate location":
        task_generate_location = Task(
            description="""Generate a detailed location for the game of Necromunda.""",
            agent=agents[0],
            expected_output="A detailed description of the generated location for Necromunda."
        )
        tasks.append(task_generate_location)

    elif user_action == "look up rules":
        user_query = input("Enter the rule you want to look up: ")
        task_lookup_rules = Task(
            description="""Look up and provide explanations for the following rule from the Necromunda rulebook: 
            {rule_query}
            """.format(rule_query=user_query),
            agent=agents[1],
            expected_output="An explanation and reference for the queried rule from the Necromunda rulebook."
        )
        tasks.append(task_lookup_rules)

    elif user_action == "simulate combat":
        if data_upload:
            task_simulate_combat = Task(
                description="""Simulate a combat round based on the following scenario details, location, factions, and gangers:
                {df}
                """.format(df=df.head()),
                agent=agents[2],
                expected_output="A detailed simulation of the combat round, including attack resolutions, damage calculations, and applied effects."
            )
        else:
            task_simulate_combat = Task(
                description="""Simulate a combat round based on a hypothetical scenario, location, factions, and gangers.""",
                agent=agents[2],
                expected_output="A detailed simulation of the combat round, including attack resolutions, damage calculations, and applied effects."
            )
        tasks.append(task_simulate_combat)

    elif user_action == "manage gang":
        task_manage_gang = Task(
            description="""Manage gang members' stats, inventory, skills, and notes. Ensure all changes are validated and up-to-date.""",
            agent=agents[3],
            expected_output="Updated records for the gang members, including any changes to stats, inventory, skills, and notes."
        )
        tasks.append(task_manage_gang)

    elif user_action == "generate scenario":
        task_generate_scenario = Task(
            description="""Generate a scenario for the game of Necromunda, considering objectives, environmental conditions, and factions involved.""",
            agent=agents[4],
            expected_output="A detailed and balanced scenario for the game of Necromunda."
        )
        tasks.append(task_generate_scenario)

    elif user_action == "roll dice":
        dice_roll_expression = input("Enter the dice roll expression (e.g., '2d6+3'): ")
        task_roll_dice = Task(
            description="""Perform the following dice roll: 
            {dice_roll}
            """.format(dice_roll=dice_roll_expression),
            agent=agents[5],
            expected_output="The result of the dice roll."
        )
        tasks.append(task_roll_dice)

    elif user_action == "manage event":
        task_manage_event = Task(
            description="""Manage an in-game event that can affect gameplay, including random events, environmental changes, or narrative-driven incidents.""",
            agent=agents[6],
            expected_output="Details and outcomes of the managed in-game event."
        )
        tasks.append(task_manage_event)

    elif user_action == "distribute loot":
        task_distribute_loot = Task(
            description="""Manage the distribution of loot after combat encounters, ensuring fair and thematic allocation of rewards.""",
            agent=agents[7],
            expected_output="A detailed account of the loot distribution, including the items allocated to each gang member."
        )
        tasks.append(task_distribute_loot)

    elif user_action == "NPC interaction":
        task_npc_interaction = Task(
            description="""Simulate interactions with NPCs, providing realistic dialogue and outcomes based on the game's context.""",
            agent=agents[8],
            expected_output="Detailed interactions with NPCs, including dialogue and outcomes."
        )
        tasks.append(task_npc_interaction)

    elif user_action == "gang downtime":
        task_gang_downtime = Task(
            description="""Manage gang activities during downtime between matches, including recovery, training, and resource management.""",
            agent=agents[9],
            expected_output="Details of gang activities during downtime, including recovery, training, and resource management."
        )
        tasks.append(task_gang_downtime)

    elif user_action == "manage campaign":
        task_manage_campaign = Task(
            description="""Manage the overall campaign, including tracking progress, managing events, and ensuring continuity and coherence throughout the campaign.""",
            agent=agents[10],
            expected_output="A detailed report on the campaign's progress, including managed events and continuity."
        )
        tasks.append(task_manage_campaign)

    return tasks
