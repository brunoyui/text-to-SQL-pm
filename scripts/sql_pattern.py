
class SQLPattern(object):
    def __init__(self, *args, **kwargs):
        self.filters = {}
        pass

    def get_filters(self):
        return self.filters

class SQLPatternEasy(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'SC': "Condition_classification == 'none' and Condition_group_classification == 'none' and Projection_aggregation == 'none'",
            'SC_FC': "Condition_classification != 'none' and Condition_group_classification == 'none' and Projection_aggregation == 'none'",
            'SC_GFC': "Condition_classification == 'none' and Condition_group_classification != 'none' and Projection_aggregation == 'none'",
            'AC': "Condition_classification == 'none' and Condition_group_classification == 'none' and Projection_aggregation != 'none'",
            'AC_FC': "Condition_classification != 'none' and Condition_group_classification == 'none' and Projection_aggregation != 'none'"
        }

class SQLPatternMedium(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'SC': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification == 'none' and Groupby == 'no'",
            'SC_GC': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification == 'none' and Groupby == 'yes'",
            'SC_FC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none'",
            'SC_GC_FC': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification != 'none'",
            'ACC_GC': "Projection_aggregation != 'none' and Condition_classification == 'none' and Condition_group_classification == 'none'",
            'ACC_FC_GC': "Projection_aggregation != 'none' and Condition_classification != 'none' and Condition_group_classification == 'none'",
            'ACC_FC_GC_FC': "Projection_aggregation != 'none' and Condition_group_classification != 'none'"
        }

class SQLPatternHard(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'SC_FC_GC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_condition == 'no' and IUEN == 'no'",
            'SC_FSC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Groupby == 'no' and Subselect_condition == 'yes' and IUEN == 'no'",
            'SC_FC_GC_FC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification != 'none' and Groupby == 'yes' and Subselect_condition == 'no' and IUEN == 'no'",
            'SC_GC_FSC': "Projection_aggregation == 'none' and Condition_classification == 'none' and Condition_group_classification != 'none' and Subselect_having == 'yes' and Groupby == 'yes' and IUEN == 'no'",
            'AC_FSC': "Projection_aggregation != 'none' and Subselect_condition == 'yes' and IUEN == 'no'",
            'ACC_FC_GC': "Projection_aggregation != 'none' and Subselect_condition == 'no' and IUEN == 'no' and Condition_classification != 'none'",
            'SIE': "IUEN == 'yes'"
        }

class SQLPatternExtra(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'SC_FC_GC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no'",
            'SC_FSC_FC_GC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Subselect_from == 'no' and Subselect_condition == 'yes'",
            'SC_FC_GC_FSC': "Projection_aggregation == 'none' and Subselect_from == 'no' and Subselect_having == 'yes'",
            'ACC_FC_GC': "Projection_aggregation != 'none' and Condition_classification != 'none' and Subselect_from == 'no' and IUEN == 'no'  and Subselect_condition == 'no'",
            'AC_FSC': "Projection_aggregation != 'none' and Condition_classification != 'none' and Subselect_from == 'no' and IUEN == 'no'  and Subselect_condition == 'yes'",
            'ACC_GC_FSC': "Projection_aggregation != 'none' and Condition_classification == 'none' and Subselect_from == 'no' and IUEN == 'no'",
            'SU': "IUEN == 'yes'"
        }   

class SQLPatternNoHardness(SQLPattern):
    def __init__(self, *args, **kwargs):
        self.filters = {
            'SC_FC_GC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no' and Subselect_with == 'no'",
            'SC_GC_FC': "Projection_aggregation == 'none' and Condition_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no'",
            'SC_FC_FSC_GC': "Projection_aggregation == 'none' and Condition_classification != 'none' and Subselect_from == 'no' and Subselect_condition == 'yes'",
            'SC_RS_FC': "Projection_aggregation == 'none' and Subselect_from == 'yes'",
            'ACC_FC_GC': "Projection_aggregation != 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'no' and IUEN == 'no'",
            'ACC_FSC_GC': "Projection_aggregation != 'none' and Condition_classification != 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_condition == 'yes'",
            'ACC_GC': "Projection_aggregation != 'none' and Condition_classification == 'none' and Condition_group_classification == 'none' and Subselect_from == 'no' and Subselect_with == 'no'",
            'ACC_RS_FC_GC': "Projection_aggregation != 'none' and Subselect_from == 'yes'",
            'SUE': "IUEN == 'yes' and Subselect_condition == 'no' and Subselect_from == 'no'",
            'WS': "Subselect_with == 'yes'"
        }