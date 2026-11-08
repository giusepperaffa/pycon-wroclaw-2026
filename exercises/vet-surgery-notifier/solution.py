# =====================
# Import Python Modules
# =====================
import unittest
from unittest.mock import patch

import db_interface
import notification_services
import vet_surgery_notifier 


class TestVetSurgeryNotifier(unittest.TestCase):
    @patch("notification_services.send_email")
    @patch("db_interface.get_active_subscriptions")
    def test_db_exception(self, mock_get_active_subscriptions, mock_send_email):
        mock_get_active_subscriptions.side_effect = db_interface.FailedDatabaseConnection
        notifier = vet_surgery_notifier.VetSurgeryNotifier()
        notifier.send_notifications()
        mock_get_active_subscriptions.assert_called_once()
        mock_send_email.assert_not_called()

    @patch("notification_services.send_email")
    def test_no_record_from_db(self, mock_send_email):
        with patch("db_interface.get_active_subscriptions") as mock_get_active_subscriptions:
            mock_get_active_subscriptions.return_value = []
            notifier = vet_surgery_notifier.VetSurgeryNotifier()
            notifier.send_notifications()
            mock_get_active_subscriptions.assert_called_once()
            mock_send_email.assert_not_called()

    @patch("notification_services.send_email")
    def test_two_records_from_db(self, mock_send_email):
        with patch("db_interface.get_active_subscriptions") as mock_get_active_subscriptions:
            mock_get_active_subscriptions.return_value = [{"owner": "Peter", "pet_type": "cat",
                "expired_vaccine": "Yes", "email_address": "peter@gmail.com"},
                {"owner": "Tom", "pet_type": "dog", "expired_vaccine": "No",
                "email_address": "tom@hotmail.com"}]
            notifier = vet_surgery_notifier.VetSurgeryNotifier()
            notifier.send_notifications()
            mock_get_active_subscriptions.assert_called_once()
            mock_send_email.assert_called_once_with("peter@gmail.com",
                "Hi Peter, your cat vaccination is now due")

            
if __name__ == "__main__":
    unittest.main()

