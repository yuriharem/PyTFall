init -5 python:
    class CleaningJob(Job):
        def __init__(self):
            super(CleaningJob, self).__init__()
            self.id = "Cleaning"
            self.type = "Service"

            # Traits/Job-types associated with this job:
            self.occupations = ["Service"] # General Strings likes SIW, Warrior, Server...
            self.occupation_traits = [traits["Maid"]] # Corresponding traits...

            # Relevant skills and stats:
            self.base_skills = {"cleaning": 100}
            self.base_stats = {"agility": 30, "constitution": 30}

        def traits_and_effects_effectiveness_mod(self, worker, log):
            """Affects worker's effectiveness during one turn. Should be added to effectiveness calculated by the function below.
               Calculates only once per turn, in the very beginning.
            """
            effectiveness = 0
             # effects always work
            if worker.effects['Food Poisoning']['active']:
                log.append("%s suffers from Food Poisoning, and is very far from her top shape." % worker.name)
                effectiveness -= 50
            elif worker.effects['Down with Cold']['active']:
                log.append("%s is not feeling well due to colds..." % worker.name)
                effectiveness -= 15

            if locked_dice(65): # traits don't always work, even with high amount of traits there are normal days when performance is not affected

                traits = list(i for i in worker.traits if i in ["Adventurous", "Homebody", "Neat", "Messy", "Shy", "Curious", "Indifferent", "Energetic"])
                if traits:
                    trait = random.choice(traits)
                else:
                    return effectiveness

                if trait == "Adventurous":
                    log.append("%s would prefer to explore dungeons and look for treasures rather than clean stuff..." % worker.name)
                    effectiveness -= 25
                elif trait == "Homebody" or trait == "Indifferent":
                    log.append("%s really enjoys the simple and predictable cleaning task." % worker.name)
                    effectiveness += 25
                elif trait == "Neat":
                    log.append("%s diligently gets rid of even slightest traces of dirt. Refreshing to see someone who truly enjoys her work." % worker.name)
                    effectiveness += 40
                elif trait == "Messy":
                    log.append("%s reluctantly does her job, preferring to hide the dirt instead of cleaning it properly." % worker.name)
                    effectiveness += 40
                elif trait == "Shy":
                    log.append("%s appreciates the chance to have a job far away from customers, where her shyness doesn't get in the way." % worker.name)
                    effectiveness += 15
                elif trait == "Curious" or trait == "Energetic":
                    log.append("%s finds the cleaning duties too boring and repetitive to perform them properly." % worker.name)
                    effectiveness -= 15
            return effectiveness

        def calculate_disposition_level(self, worker): # calculating the needed level of disposition
            sub = check_submissivity(worker)
            if "Shy" in worker.traits:
                disposition = 150 + 50 * sub
            else:
                disposition = 200 + 50 * sub
            if check_lovers(hero, worker):
                disposition -= 50
            elif check_friends(hero, worker):
                disposition -= 20
            if "Natural Follower" in worker.traits:
                disposition -= 25
            elif "Natural Leader" in worker.traits:
                disposition += 25
            if "Neat" in worker.traits:
                disposition -= 50
            if "Messy" in worker.traits:
                disposition += 100
            return disposition

        def settle_workers_disposition(self, worker, log):
            if not("Maid" in worker.traits):
                sub = check_submissivity(worker)
                if worker.status != 'slave':
                    if sub < 0:
                        if dice(15):
                            worker.logws('character', 1)
                        log.append("%s is not very happy with her current job as a cleaner, but she will get the job done." % worker.name)
                    elif sub == 0:
                        if dice(25):
                            worker.logws('character', 1)
                        log.append("%s serves customers as a cleaner, but, truth be told, she would prefer to do something else." % worker.nickname)
                    else:
                        if dice(35):
                            worker.logws('character', 1)
                        log.append("%s makes it clear that she wants another job before beginning the cleaning." % worker.name)
                    worker.logws("joy", -randint(3, 5))
                    worker.logws("disposition", -randint(5, 10))
                    worker.logws('vitality', -randint(2, 5)) # a small vitality penalty for wrong job
                else:
                    if sub < 0:
                        if worker.disposition < self.calculate_disposition_level(worker):
                            log.append("%s is a slave so no one really cares but, being forced to work as a cleaner, she's quite upset." % worker.name)
                        else:
                            log.append("%s will do as she is told, but doesn't mean that she'll be happy about her cleaning duties." % worker.name)
                        if dice(25):
                            worker.logws('character', 1)
                    elif sub == 0:
                        if worker.disposition < self.calculate_disposition_level(worker):
                            log.append("%s will do as you command, but she will hate every second of her cleaning shift..." % worker.name)
                        else:
                            log.append("%s was very displeased by her order to work as a cleaner, but didn't dare to refuse." % worker.name)
                        if dice(35):
                            worker.logws('character', 1)
                    else:
                        if worker.disposition < self.calculate_disposition_level(worker):
                            log.append("%s was very displeased by her order to work as a cleaner, and makes it clear for everyone before getting busy with clients." % worker.name)
                        else:
                            log.append("%s will do as you command and work as a cleaner, but not without a lot of grumbling and complaining." % worker.name)
                        if dice(45):
                            worker.logws('character', 1)
                    if worker.disposition < self.calculate_disposition_level(worker):
                        worker.logws("joy", -randint(4, 8))
                        worker.logws("disposition", -randint(5, 10))
                        worker.logws('vitality', -randint(5, 10))
                    else:
                        worker.logws("joy", -randint(2, 4))
                        worker.logws('vitality', -randint(1, 4))
            else:
                log.append(choice(["%s is doing her shift as a cleaner." % worker.name, "%s gets busy with cleaning." % worker.fullname]))
            return True
