from numpy import mean, max, min, unique

class PalleteGenerator:

    def __init__(self):
        self.pallete = []

    def median_cut(self, img_array):
        r_average = round(mean(img_array[:, 0]))
        g_average = round(mean(img_array[:, 1]))
        b_average = round(mean(img_array[:, 2]))
        value = [r_average, g_average, b_average]
        self.pallete.append(value)

    def split_into_buckets(self, img_array, depth):

        if len(img_array) == 0:
            return

        if depth == 0:
            self.median_cut(img_array)
            return

        r_range = max(img_array[:, 0]) - min(img_array[:, 0])
        g_range = max(img_array[:, 1]) - min(img_array[:, 1])
        b_range = max(img_array[:, 2]) - min(img_array[:, 2])

        space_with_highest_range = 0

        if g_range >= r_range and g_range >= b_range:
            space_with_highest_range = 1
        elif b_range >= r_range and b_range >= g_range:
            space_with_highest_range = 2

        # No need to check r_range since the variable starts at 0

        img_array = img_array[img_array[:, space_with_highest_range].argsort()]
        # self.median_cut(img_array)

        median_index = int((len(img_array) + 1) / 2)
        img_array_1 = img_array[0:median_index]
        img_array_2 = img_array[median_index:]

        # del img_array

        self.split_into_buckets(img_array_1, depth - 1)
        self.split_into_buckets(img_array_2, depth - 1)

    def flatten_img_array(self, img_array):
        return unique(img_array.reshape(-1, img_array.shape[2]), axis=0)

    def generate_pallete(self, img_array, depth):
        flattened_array = self.flatten_img_array(img_array)
        self.split_into_buckets(flattened_array, depth)
        return self.pallete
