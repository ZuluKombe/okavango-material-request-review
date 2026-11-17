# OKAVANGO_AUTO_MR_ISSUE_BEGIN - v2: clone-only, feature-flagged.
# Add handlers without discarding other app hooks.
if "doc_events" not in globals():
    doc_events = {}
def _okavango_mr_v2_register(doctype, event, handler):
    existing = doc_events.setdefault(doctype, {})
    prior = existing.get(event)
    if not prior:
        existing[event] = handler
    elif isinstance(prior, (tuple, list)):
        if handler not in prior:
            existing[event] = list(prior) + [handler]
    elif handler != prior:
        existing[event] = [prior, handler]
_okavango_mr_v2_register("Material Request", "on_submit", "okavango_enhancements.automatic_material_issue.on_material_request_submit")
_okavango_mr_v2_register("Material Request", "before_cancel", "okavango_enhancements.automatic_material_issue.before_material_request_cancel")
_okavango_mr_v2_register("Stock Entry", "before_cancel", "okavango_enhancements.automatic_material_issue.before_automatic_stock_entry_cancel")
# OKAVANGO_AUTO_MR_ISSUE_END
