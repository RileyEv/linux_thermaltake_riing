"""
linux_thermaltake_rgb
Software to control your thermaltake hardware
Copyright (C) 2018  Max Chesterfield (chestm007@hotmail.com)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
from linux_thermaltake_rgb.devices import ThermaltakeRGBDevice, ThermaltakeFanDevice


class ThermaltakeRiingPlusFan(ThermaltakeRGBDevice, ThermaltakeFanDevice):
    model = "Riing Plus"
    num_leds = 12
    index_per_led = 3


class ThermaltakeRiingQuadFan(ThermaltakeRGBDevice, ThermaltakeFanDevice):
    model = "Riing Quad"
    num_leds = 54
    index_per_led = 3

    def set_lighting(self, values: list = None, mode=0x18, speed=0x00) -> None:
        super().set_lighting(values, mode, speed)
        self.controller.driver.read_in()
