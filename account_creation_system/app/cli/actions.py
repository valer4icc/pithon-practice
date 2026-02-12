from app.services.registration import register_user
from app.reports.tables import show_users_table
from app.reports.stats import show_statistics
from app.reports.domains import show_domain_report
from app.features.search import search_user_by_username
from app.features.lists import show_usernames, show_adults, show_emails
from app.features.sorting import show_users_sorted_by_age

def get_actions():
    return {
        1: register_user,
        2: show_users_table,
        3: search_user_by_username,
        4: show_statistics,
        5: show_usernames,
        6: show_domain_report,
        7: show_adults,
        8: show_emails,
        9: show_users_sorted_by_age
    }
