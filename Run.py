import Parameter as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.LDCT)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with HIV',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'LDCT Screening:')



cohort_PLCO = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.PLCO)

# simulate the cohort
simOutputs_PLCO = cohort_PLCO.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs_PLCO.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs_PLCO.get_survival_times(),
    title='Survival times of patients with HIV',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs_PLCO, 'PLCO Screening:')
