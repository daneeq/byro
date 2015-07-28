#!/usr/bin/env python3

import os
import unittest
from byro.mail import Mail


def get_test_files_dir():
        return os.path.realpath(os.path.dirname(__file__)) + "/data/"


class Recipients(unittest.TestCase):

    def test_mail(self):
        mail = "john.doe@example.com"
        returned = Mail._read_recipients_from_file(mail)
        expected = [mail]
        self.assertEqual(returned, expected)

    def test_file(self):
        filename = get_test_files_dir()
        filename += "recipients.txt"
        rec_ac = Mail._read_recipients_from_file(filename)
        rec_ex = ["email@example.com", "email@example.cz", "email@example.eu"]
        self.assertEqual(rec_ac, rec_ex)


class Body(unittest.TestCase):

    def test_simple(self):
        path = get_test_files_dir()
        filename = path + "simple-body.md"
        returned = Mail._read_markdown_body(filename)

        expected = "Dobrý den,\n\ndovoluji se Vás oslovit ve věci mimořádné důležitosti."
        self.assertEqual(returned['raw'], expected)

        expected = "<p>Dobrý den,</p>\n<p>dovoluji se Vás oslovit ve věci mimořádné důležitosti.</p>"
        self.assertEqual(returned['html'], expected)

        self.assertEqual(returned['meta'], {})

    def test_advance(self):
        path = get_test_files_dir()
        filename = path + "advance-body.md"
        returned = Mail._read_markdown_body(filename)

        expected = "---\nSubject: Hello world!\n---\n\n\nHello world\n===========\n\n**bold**\n\n*italic*\n\n[some link](www.example.com)"
        self.assertEqual(returned['raw'], expected)