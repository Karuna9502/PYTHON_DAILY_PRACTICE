class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        source_index = -1
        dest_position = 0
        while dest_position < n:
            source_index += 1
            if arr[source_index] == 0:
                dest_position += 2
            else:
                dest_position += 1
        write_position = n - 1
        if dest_position == n + 1:
            arr[write_position] = 0
            source_index -= 1
            write_position -= 1
        while write_position >= 0:
            if arr[source_index] == 0:
                arr[write_position] = 0
                arr[write_position - 1] = 0
                write_position -= 1
            else:
                arr[write_position] = arr[source_index]
            source_index -= 1
            write_position -= 1
