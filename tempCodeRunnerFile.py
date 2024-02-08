    if orientation == Qt.Horizontal and role == Qt.DisplayRole:  # Orientation is horizontal header
            if section == 1:  # For the Status column
                return "Status"
            elif section == 2:  # For the Size column
                return "Size"
            elif section == 3:  # For the Type column
                return "Type"
            elif section == 4:  # For the Date Modified column
                return "Date Modified"
        return super().headerData(section, orientation, role)