from django.contrib import admin
from django.utils.http import urlencode


class MultiSelectRelatedFieldListFilter(admin.RelatedFieldListFilter):
    """
    Custom filter that allows selecting multiple related field values (tags).
    Doesn't look perfect
    """

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = "%s__in" % field_path
        super().__init__(field, request, params, model, model_admin, field_path)
        # Manually set some params
        self.lookup_kwarg = "%s__in" % field_path
        self.field_path = 'tags__in'

    def choices(self, changelist):
        # Include <All> and <->
        params = changelist.get_filters_params()
        selected_param = params.get(self.field_path, [])

        yield {
            "selected": not selected_param and not self.lookup_val_isnull,
            "query_string": changelist.get_query_string(
                remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]
            ),
            "display": "All",
        }

        selected_values = set(selected_param[0].split(',')) if selected_param else set()

        for lookup, title in self.lookup_choices:
            lookup_str = str(lookup)
            new_values = selected_values ^ {lookup_str}  # Toggle selection

            new_params = params.copy()
            new_params.pop(self.lookup_kwarg_isnull, None)
            if new_values:
                new_params[self.field_path] = ",".join(new_values)
            else:
                new_params.pop(self.field_path, None)

            yield {
                "selected": lookup_str in selected_values,
                "query_string": "?" + urlencode(new_params, doseq=True),
                "display": title,
            }

        empty_title = self.empty_value_display
        if self.include_empty_choice:
            yield {
                "selected": bool(self.lookup_val_isnull),
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg_isnull: "True"}, [self.lookup_kwarg]
                ),
                "display": empty_title,
            }
