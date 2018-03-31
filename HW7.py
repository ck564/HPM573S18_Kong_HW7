import SurvivalModelClasses as SurvivalModel
from scipy.stats import binom

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort

# create a cohort of patients
myCohort = SurvivalModel.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)

# Problem 1: print percentage of patients survived beyond 5 years
print('Percentage of patients survived beyond 5 years (q):', myCohort.get_percentage_survival_5()*100,
      '%')

# Problem 2:
print('The binomial distribution would seem appropriate for the probability of the number ' 
      'of participants that survived beyond 5 years in a cohort of N participants')

# Problem 3:
k, n, p = 400, 500, 0.5
print('Likelihood of 5-year survival for 400/573 participants if survival is expected to be 50%:', binom.pmf(k, n, p))

