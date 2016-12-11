# -*- coding: utf-8 -*-
# Copyright (c) 2015, eSwitch and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.password import get_decrypted_password

class BPSSettings(Document):
	def validate(self):
		pass
		# self.bps_password_value = self.bps_password
		# self.bps_password_value = get_decrypted_password('BPS Settings', 'BPS Settings', 'bps_password',
		# 										False)

# @frappe.whitelist(allow_guest=False)
# def display_readonly(doc):
# 	data = frappe.get_doc("MTN Services Settings")
# 	data.ussd_password = get_decrypted_password('MTN Services Settings', 'MTN Services Settings', 'ussd_password',
# 												False)