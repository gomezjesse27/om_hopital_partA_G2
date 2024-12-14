from odoo import fields
from odoo.tests import common, new_test_user

class TestHospitalModule(common.TransactionCase):
    def test_doctor_appointment_count(self):
        user = new_test_user(self.env, "test base user", groups = "base.group_user")

        patient = self.env["hospital.patient"].create({
            "name": "Jane Doe",
            "age": 60,
        })

        doctor = self.env["hospital.doctor"].create({
            "doctor_name": "Bob Smith",
            "gender": "male",
            "age": 50,
        })

        appointment = self.env["hospital.appointment"].create({
           "patient_id": patient.id,
           "doctor_id": doctor.id,
           "date_appointment": fields.Date.today(),
        })

        self.assertEqual(doctor.appointment_count, 1, "Appointment creation has bug, number of appointments should be 1")