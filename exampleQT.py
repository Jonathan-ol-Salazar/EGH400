#!/usr/bin/env python
# coding: utf-8

# THIS CODE IS ORIGINALLY AUTHORED BY Aleksandar Veljković



# ## Locating "area code" on the given depth in quad tree that contains specified geo point

# In[1]:


def get_area_code(lat, lon, depth = 10, lat_from = -90, lat_to = 90, lon_from = -180, lon_to = 180, code = ''):
    
    '''
    +---+---+
    | 0 | 1 |
    +---+---+
    | 2 | 3 |
    +---+---+
    '''
    
    if depth == 0:
        return (code, lat_from, lat_to, lon_from, lon_to)
    
    lat_mid = (lat_from + lat_to) / 2
    lon_mid = (lon_from + lon_to) / 2
    
    if lat < lat_mid:
        
        if lon < lon_mid:
            code += '2'
            return get_area_code(lat, lon, depth - 1, lat_from, lat_mid, lon_from, lon_mid, code)
        else:
            code += '3'
            return get_area_code(lat, lon, depth - 1, lat_from, lat_mid, lon_mid, lon_to, code)

    else:

        if lon < lon_mid:
            code += '0'
            return get_area_code(lat, lon, depth - 1, lat_mid, lat_to, lon_from, lon_mid, code)
        else:
            code += '1'
            return get_area_code(lat, lon, depth - 1, lat_mid, lat_to, lon_mid, lon_to, code)


# In[2]:


lat = 44.81946044
lon = 20.46048887
depth = 11
get_area_code(lat, lon, depth)


# ## Check if area with the given code contains specified point

# In[3]:


def check_area_code(lat, lon, code, depth, level=0, lat_from = -90, lat_to = 90, lon_from = -180, lon_to = 180):
    if level == len(code):
        if depth == 0 and lat >= lat_from and lat < lat_to and lon >= lon_from and lon < lon_to:
            return True
        return False
    
    lat_mid = (lat_from + lat_to) / 2
    lon_mid = (lon_from + lon_to) / 2
    
    if code[level] == '2':
        return check_area_code(lat, lon, code, depth - 1, level + 1, lat_from, lat_mid, lon_from, lon_mid)
    
    if code[level] == '3':
        return check_area_code(lat, lon, code, depth - 1, level + 1, lat_from, lat_mid, lon_mid, lon_to)
    
    if code[level] == '0':
        return check_area_code(lat, lon, code, depth - 1, level + 1, lat_mid, lat_to, lon_from, lon_mid)
    
    if code[level] == '1':
        return check_area_code(lat, lon, code, depth - 1, level + 1, lat_mid, lat_to, lon_mid, lon_to)


# In[4]:


check_area_code(lat, lon, '12001110120', depth)


# ## Get the lowest common ancestor of a nodes (areas) with the given codes in the quad tree

# In[5]:


def get_smallest_common_area(codes):
    n = len(codes[0])
    m = len(codes)
    
    lca = ''
    
    for i in range(n):
        for j in range(1, m):
            if codes[j][i] != codes[0][i]:
                return lca
        lca += codes[0][i]
        
    return lca


# In[6]:


codes = ['02233323022', '02233323021', '02233323032']
get_smallest_common_area(codes)


# ## Wrapped up in one class
# One area contains an array of airspace reservations in that area. The reservations are sorted ascending by the reservation end time. Reservation requests contain 3D volume points, starting and ending timestamps and reservation status. Adding new reservaition is done by:
# - finding all areas that contain reservation volume points
# - finding all parent nodes of found areas
# - getting all reservations (from those areas' (sorted) arrays) that do not end before new reservation and that do not start until new reservation has expired.
# - running collision check to check for possible collisions with previous reservation in the given areas

# In[7]:


class Request:
    def __init__(self, volume, time_from, time_to):
        self.volume = volume
        self.time_from = time_from
        self.time_to = time_to
        self.status = 'PENDING'

class AirspaceService:
    def __init__(self, depth):
        self.areas = {}
        self.depth = depth
        
    # Create new reservation
    def request_reservation(self, request):
        volume = request.volume
        time_from = request.time_from
        time_to = request.time_to
        
        area_codes = set([])

        for vertex in volume:
            area_codes.add(self.get_area_code(vertex[0], vertex[1], self.depth)[0])
            
        sca = self.get_smallest_common_area(list(area_codes))
        
        if sca not in self.areas:
            self.areas[sca] = []
                
        if not self.has_collision(volume, time_from, time_to, sca):
            request.status = 'APPROVED'
            
            n = len(sca)

            for i in range(1, n):
                if sca[:i] not in self.areas:
                    self.areas[sca[:i]] = []
            
            self.add_to_area(sca, request)
            
            return True            
        else:
            request.status = 'DECLINED'
            self.areas[sca].append(request)
            return False
        
    # add new volume to area
    def add_to_area(self, code, request):
        n = len(self.areas[code])
        
        for i in range(n - 1, -1, -1):
            check_area = self.areas[code][i]
            
            if check_area.time_to <= request.time_to:
                self.areas[code].insert(i + 1, request)
                return
        
        self.areas[code].insert(0, request)
             
        
    # Get all nodes in tree from node to the given area code
    def get_areas_on_path(self, code, time_from, time_to, level = 0, current_code = '', status_filter='APPROVED'):
        # Ugly piece of code starts here
        if level == self.depth:
            return []
        
        flood = True
        
        if level < len(code):
            flood = False
            current_code += code[level]
            
        if current_code not in self.areas:
            return []
        
        # TODO: Implement this filter in separate function
        m = len(self.areas[current_code])
        current_array = []

        for j in range(m - 1, 0, -1):
            check_area = self.areas[current_code][j]
            if check_area.time_to < time_from:
                break
            if check_area.status == status_filter:
                current_array.append(check_area)
        
        if not flood:
            res = self.get_areas_on_path(code, time_from, time_to, level + 1, current_code)
            return current_array + res
        else:
            if current_code == code:
                current_array = []
                
            res1 =  self.get_areas_on_path(code, time_from, time_to, level + 1, current_code + '0')
            res2 = self.get_areas_on_path(code, time_from, time_to, level + 1, current_code + '1')
            res3 = self.get_areas_on_path(code, time_from, time_to, level + 1, current_code + '2')
            res4 = self.get_areas_on_path(code, time_from, time_to, level + 1, current_code + '3')
            
            return current_array + res1 + res2 + res3 + res4
        
    # Check for possible collisions
    def has_collision(self, volume_hull, time_from, time_to, code):
        # Get all colliding candidates
     #   possible_collisions = self.get_areas_on_path(code, time_from, time_to)

        # TODO: Check possible colisions
        
        return False
            
    def get_smallest_common_area(self, codes):
        n = len(codes[0])
        m = len(codes)

        sca = ''

        for i in range(n):
            for j in range(1, m):
                if codes[j][i] != codes[0][i]:
                    return sca
            sca += codes[0][i]

        return sca
            
    def get_area_code(self, lat, lon, depth = 10, lat_from = -90, lat_to = 90, lon_from = -180, lon_to = 180, code = ''):

        '''
        +---+---+
        | 0 | 1 |
        +---+---+
        | 2 | 3 |
        +---+---+
        '''

        if depth == 0:
            return (code, lat_from, lat_to, lon_from, lon_to)

        lat_mid = (lat_from + lat_to) / 2
        lon_mid = (lon_from + lon_to) / 2

        if lat < lat_mid:

            if lon < lon_mid:
                code += '2'
                return get_area_code(lat, lon, depth - 1, lat_from, lat_mid, lon_from, lon_mid, code)
            else:
                code += '3'
                return get_area_code(lat, lon, depth - 1, lat_from, lat_mid, lon_mid, lon_to, code)

        else:

            if lon < lon_mid:
                code += '0'
                return get_area_code(lat, lon, depth - 1, lat_mid, lat_to, lon_from, lon_mid, code)
            else:
                code += '1'
                return get_area_code(lat, lon, depth - 1, lat_mid, lat_to, lon_mid, lon_to, code)


    def check_area_code(self, lat, lon, code, depth, level=0, lat_from = -90, lat_to = 90, lon_from = -180, lon_to = 180):
        if level == len(code):
            if depth == 0 and lat >= lat_from and lat < lat_to and lon >= lon_from and lon < lon_to:
                return True
            return False

        lat_mid = (lat_from + lat_to) / 2
        lon_mid = (lon_from + lon_to) / 2

        if code[level] == '2':
            return check_area_code(lat, lon, code, depth - 1, level + 1, lat_from, lat_mid, lon_from, lon_mid)

        if code[level] == '3':
            return check_area_code(lat, lon, code, depth - 1, level + 1, lat_from, lat_mid, lon_mid, lon_to)

        if code[level] == '0':
            return check_area_code(lat, lon, code, depth - 1, level + 1, lat_mid, lat_to, lon_from, lon_mid)

        if code[level] == '1':
            return check_area_code(lat, lon, code, depth - 1, level + 1, lat_mid, lat_to, lon_mid, lon_to)        
        
    def get_airspace(self):
        return self.areas


# In[8]:


# Tests

volume = [[44,20,2],[44,20.3,2], [43.9,19.99,3]]
time_from = 1234567
time_to = 1234590 

r1 = Request(volume, time_from, time_to)

volume = [[44,20,2],[44,20.3,2], [43.9,19.99,3]]
time_from = 123455
time_to = 1234592

r2 = Request(volume, time_from, time_to)

volume = [[44,20,2],[44,20.3,2], [43.9,19.99,3]]
time_from = 123440
time_to = 1234580

r3 = Request(volume, time_from, time_to)

airspace_service = AirspaceService(depth = 12)
airspace_service.request_reservation(r2)
airspace_service.request_reservation(r1) 
airspace_service.request_reservation(r3)
print(airspace_service.get_airspace())
airspace_service.get_areas_on_path('12001112', 1234580, 1234591)
# airspace_service.areas['02233302'] = [r]
# airspace_service.get_areas_on_path('0223330', 0, 1)

print(airspace_service.get_airspace()['12001112'][0].time_to)
print(airspace_service.get_airspace()['12001112'][1].time_to)
print(airspace_service.get_airspace()['12001112'][2].time_to)

