#!/usr/bin/env python
# -*- coding: gb2312 -*-
#
#  pi_function.py
#  
#  Copyright 2017 Administrator <Administrator@WIN-84KOMAOFRMQ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import math

def make_random_list(m,a,c,s0):
	"""����ͬ�෨����α�������"""
	s = []
	s.append(s0)
	s_float = []
	s_float.append(s[0]/m)
	i = 0
	while i < m:
		 s.append((s[i]*a+c)%m)
		 s_float.append(s[i+1]/m)
		 i += 1
	return s_float

def compute_pi(sx,sy,m):
	"""����pi��ֵ"""
	#~ s_len = len(sx)
	count = 0
	i = 0
	while i < m:
		if math.sqrt(sx[i]*sx[i] + sy[i]*sy[i]) < 1:
			count += 1
		i += 1
	pi = 4 * count / m
	return pi
	
if __name__ == "__main__":
	pi_sum = 0.0
	#~ k1 = 3
	#~ k2 = 5
	k_list = [3,5,7,11,13,17,19,23,31,37]
	total_times = 1
	m = 65536 * 2
	c = 5
	s0 = 1
	i = 0
	while i < total_times:
		k1 = k_list[i]
		k2 = k_list[i+1]
		j = 0
		pi_true = 3.14159265
		pi_min = 3
		while j < 1000:
			
			sx = make_random_list(m,4*k1+1,c,s0+j)
			sy = make_random_list(m,4*k2+1,c,s0)
			pi = compute_pi(sx,sy,m)
			if abs(pi-pi_true) < abs(pi_min-pi_true):
				pi_min = pi
			#~ print(pi_min)
			j += 1
		print(pi_min)
		#~ print(pi)
		pi_sum += pi
		#~ k1 += 2
		#~ k2 += 2
		i += 1
		
	print(pi_sum/total_times)
	print(1/3)
