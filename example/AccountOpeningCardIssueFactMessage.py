#!/usr/bin/env python3
from types.FactMessage import FactMessage
from decorators.FactMessageDecorator import fact_message


@fact_message(validated_by="AccountOpeningCardIssueRule")
class AccountOpeningCardIssueFactMessage(FactMessage):
    def __init__(self, facts):
        self.facts = facts
