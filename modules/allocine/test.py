# -*- coding: utf-8 -*-

# Copyright(C) 2013 Julien Veyssier
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

from weboob.tools.test import BackendTest


class AllocineTest(BackendTest):
    BACKEND = 'allocine'

    def test_search_movie(self):
        movies = list(self.backend.iter_movies('spiderman'))
        for movie in movies:
            assert movie.id

    def test_get_movie(self):
        movie = self.backend.get_movie('5032')
        assert movie.id
        assert movie.original_title

    def test_search_person(self):
        persons = list(self.backend.iter_persons('dewaere'))
        for person in persons:
            assert person.id

    def test_get_person(self):
        person = self.backend.get_person('1116')
        assert person.id
        assert person.name
        assert person.birth_date

    def test_movie_persons(self):
        persons = list(self.backend.iter_movie_persons('5032'))
        for person in persons:
            assert person.id
            assert person.name

    def test_person_movies(self):
        movies = list(self.backend.iter_person_movies('1115'))
        for movie in movies:
            assert movie.id
            assert movie.original_title
