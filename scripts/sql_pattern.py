
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
    