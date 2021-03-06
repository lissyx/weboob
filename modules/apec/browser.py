# -*- coding: utf-8 -*-

# Copyright(C) 2013      Bezleputh
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

from weboob.tools.browser.decorators import id2url
from weboob.tools.browser import BaseBrowser

from .pages import SearchPage, AdvertPage
from .job import ApecJobAdvert


__all__ = ['ApecBrowser']


class ApecBrowser(BaseBrowser):
    PROTOCOL = 'http'
    DOMAIN = 'www.apec.fr'
    ENCODING = None

    PAGES = {
        'http://cadres.apec.fr/liste-offres-emploi-cadres/8_0___(.*?)_(.*?)_(.*?)_(.*?)_(.*?)_(.*?)_(.*?)_offre-d-emploi.html': SearchPage,
        'http://cadres.apec.fr/MesOffres/RechercheOffres/ApecRechercheOffre.jsp\?keywords=(.*?)': SearchPage,
        'http://cadres.apec.fr/offres-emploi-cadres/offres-emploi-cadres/\d*_\d*_\d*_(.*?)________(.*?).html(.*?)': AdvertPage,
    }

    def search_job(self, pattern=None, region=None, fonction=None, secteur=None, salaire=None, contrat=None, limit_date=None, level=None):
        if pattern:
            self.location('http://cadres.apec.fr/MesOffres/RechercheOffres/ApecRechercheOffre.jsp?keywords=%s'
                          % pattern.replace(' ', '+'))
        else:
            self.location(
                'http://cadres.apec.fr/liste-offres-emploi-cadres/8_0___%s_%s_%s_%s_%s_%s_%s_offre-d-emploi.html'
                % (
                    region,
                    fonction,
                    secteur,
                    salaire,
                    level,
                    limit_date,
                    contrat
                ))
        assert self.is_on_page(SearchPage)
        return self.page.iter_job_adverts()

    @id2url(ApecJobAdvert.id2url)
    def get_job_advert(self, url, advert):
        self.location(url)
        assert self.is_on_page(AdvertPage)
        return self.page.get_job_advert(url, advert)
