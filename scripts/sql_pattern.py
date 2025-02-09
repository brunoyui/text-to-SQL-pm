
class SQLPattern(object):
    def __init__(self, *args, **kwargs):
        self.filters = {}
        pass

    def get_filters(self):
        return self.filters

class SQLPatternEasy(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'Sc': "Condition_classification == 'none' and Condition_group_classification == 'none' and Projection_aggregation == 'none'",
            'ScFc': "Condition_classification != 'none' and Condition_group_classification == 'none' and Projection_aggregation == 'none'",
            'ScGcFc$^+$': "Condition_classification == 'none' and Condition_group_classification != 'none' and Projection_aggregation == 'none'",
            'Ac': "Condition_classification == 'none' and Condition_group_classification == 'none' and Projection_aggregation != 'none'",
            'AcFc': "Condition_classification != 'none' and Condition_group_classification == 'none' and Projection_aggregation != 'none'"
        }

class SQLPatternMedium(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'Sc$^+$': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification == 'none' and Groupby == 'no'",
            'ScGc': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification == 'none' and Groupby == 'yes'",
            'Sc$^+$Fc$^+$': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none'",
            'Sc$^+$GcFc$^+$': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification != 'none'",
            'Acc$^+$Gc': "Projection_aggregation != 'none' and Condition_classification == 'none' and Condition_group_classification == 'none'",
            'Ac(c$^+$)$^*$Fc$^+$(Gc)$^*$': "Projection_aggregation != 'none' and Condition_classification != 'none' and Condition_group_classification == 'none'",
            '(Ac)$^+$c(Fc)$^*$GcFc': "Projection_aggregation != 'none' and Condition_group_classification != 'none'"
        }

class SQLPatternHard(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'Sc$^+$Fc$^+$(Gc)$^*$': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_condition == 'no' and IUEN == 'no'",
            'ScFsc': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Groupby == 'no' and Subselect_condition == 'yes' and IUEN == 'no'",
            'ScFcGcFc': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification != 'none' and Groupby == 'yes' and Subselect_condition == 'no' and IUEN == 'no'",
            'ScGcFsc': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification != 'none' and Subselect_having == 'yes' and Groupby == 'yes' and IUEN == 'no'",
            'AcFsc': "Projection_aggregation != 'none' and Subselect_condition == 'yes' and IUEN == 'no'",
            'AccFc$^+$Gc': "Projection_aggregation != 'none' and Subselect_condition == 'no' and IUEN == 'no' and Condition_classification != 'none'",
            'SIE': "IUEN == 'yes'"
        }

class SQLPatternExtra(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'ScFc$^+$(Gc)$^*$': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no'",
            'ScFsc(Fc)$^*$(Gc)$^*$': "Projection_aggregation == 'none' and Condition_classification != 'none' and Subselect_from == 'no' and Subselect_condition == 'yes'",
            'Sc(Fc)$^*$GcFsc': "Projection_aggregation == 'none' and Subselect_from == 'no' and Subselect_having == 'yes'",
            'Acc$^+$Fc$^+$Gc$^+$': "Projection_aggregation != 'none' and Condition_classification != 'none' and Subselect_from == 'no' and IUEN == 'no'  and Subselect_condition == 'no'",
            'AcFsc': "Projection_aggregation != 'none' and Condition_classification != 'none' and Subselect_from == 'no' and IUEN == 'no'  and Subselect_condition == 'yes'",
            'AccGc(Fsc)$^*$': "Projection_aggregation != 'none' and Condition_classification == 'none' and Subselect_from == 'no' and IUEN == 'no'",
            'SU': "IUEN == 'yes'"
        }   

class SQLPatternNoHardness(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'Sc$^+$Fc$^+$(Gc)$^*$': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no' and Subselect_with == 'no'",
            'Sc$^+$Gc(Fc)$^*$': "Projection_aggregation == 'none' and Condition_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no'",
            'Sc$^+$(Fc)$^*$Fsc(Gc)$^*$': "Projection_aggregation == 'none' and Condition_classification != 'none' and Subselect_from == 'no' and Subselect_condition == 'yes'",
            'Sc$^+$RS(Fc)$^*$': "Projection_aggregation == 'none' and Subselect_from == 'yes'",
            'Ac(c)$^*$Fc$^+$(Gc)$^*$': "Projection_aggregation != 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no'",
            'AccFscGc': "Projection_aggregation != 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'yes'",
            'AccGc': "Projection_aggregation != 'none' and Condition_classification == 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_with == 'no'",
            'Ac(c)$^*$RS(Fc)$^*$(Gc)$^*$': "Projection_aggregation != 'none' and Subselect_from == 'yes'",
            'S(UE)$^+$': "IUEN == 'yes' and Subselect_condition == 'no' and Subselect_from == 'no'",
            'WS': "Subselect_with == 'yes'"
        }