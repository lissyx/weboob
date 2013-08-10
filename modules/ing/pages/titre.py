# -*- coding: utf-8 -*-

# Copyright(C) 2013  Florent Fourcot
#
# This file is part of weboob.
#
# weboob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# weboob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with weboob. If not, see <http://www.gnu.org/licenses/>.


from decimal import Decimal

from weboob.capabilities.bank import Investment
from weboob.tools.browser import BasePage
from weboob.tools.capabilities.bank.transactions import FrenchTransaction

__all__ = ['TitrePage']


class TitrePage(BasePage):
    def on_loaded(self):
        pass

    def iter_investments(self):
        # We did not get some html, but something like that (XX is a quantity, YY a price):
        # message='[...]
        #popup=2{6{E:ALO{PAR{{reel{695{380{ALSTOM REGROUPT#XX#YY,YY &euro;#YY,YY &euro;#1 YYY,YY &euro;#-YYY,YY &euro;#-42,42%#-0,98 %#42,42 %#|1|AXA#cotationValeur.php?val=E:CS&amp;pl=6&amp;nc=1&amp;
        #popup=2{6{E:CS{PAR{{reel{695{380{AXA#XX#YY,YY &euro;#YY,YYY &euro;#YYY,YY &euro;#YY,YY &euro;#3,70%#42,42 %#42,42 %#|1|blablablab #cotationValeur.php?val=P:CODE&amp;pl=6&amp;nc=1&amp;
        # [...]
        text = self.parser.tostring(self.document.getroot())
        lines = text.split("popup=2")
        lines.pop(0)
        for line in lines:
            columns = line.split('#')
            code = columns[0].split('{')[2]
            invest = Investment(code)
            invest.code = code
            invest.label = columns[0].split('{')[-1]
            invest.quantity = int(columns[1])
            invest.unitprice = Decimal(FrenchTransaction.clean_amount(columns[2]))
            invest.unitvalue = Decimal(FrenchTransaction.clean_amount(columns[3]))
            invest.valuation = Decimal(FrenchTransaction.clean_amount(columns[4]))
            invest.diff = Decimal(FrenchTransaction.clean_amount(columns[5]))

            yield invest
