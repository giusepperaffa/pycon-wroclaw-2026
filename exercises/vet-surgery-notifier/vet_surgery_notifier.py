# =====================
# Import Python Modules
# =====================
from datetime import datetime

import db_interface
import notification_services


class VetSurgeryNotifier:
    def _query_db(self):
        today_date = datetime.today().isoformat()
        try:
            db_query_results = db_interface.get_active_subscriptions(today_date)
            return db_query_results
        except:
            return None

    def _get_records_with_expired_vaccine(self):
        return [record for record in self._db_query_results
            if record["expired_vaccine"] == "Yes"]

    def _email_message(self, record):
        return f"Hi {record['owner']}, your {record['pet_type']} vaccination is now due"

    def send_notifications(self):
        self._db_query_results = self._query_db()
        if self._db_query_results:
            for record in self._get_records_with_expired_vaccine():
                notification_services.send_email(record["email_address"],
                    self._email_message(record))


if __name__ == "__main__":
    vet_sugery_notifier = VetSurgeryNotifier()
    vet_sugery_notifier.send_notifications()
    
