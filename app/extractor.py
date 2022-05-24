from decimal import Decimal
from unicodedata import decimal
import xlrd
import traceback
from .models import Organization, District


def extract_excel_data(location):
    """
    :param location: uri of the excel file of users to extract from. Usually excel files are placed in the sheets folder
    Creates Organisations  from an excel sheet provided
    Sheet Fields:  facility_name Telephone
    """
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)
    
    # for row_number in range(2,sheet.utter_max_rows):
    for row_number in range(2,3):
        try:
            row_data = sheet.row_values(row_number)
        except Exception as e:
            print("Error :",e)
            break
        
        facility_name_value = row_data[1]
        district_value = row_data[6]
        phone_number_value = (row_data[9])
        latitude = float(row_data[13])
        longitude = float(row_data[14])
        
        if not facility_name_value:
            break

        try:
            district_value = District.objects.get(name__contains=district_value)
        except Exception as e:
            print(e)
            district_value,_ = District.objects.get_or_create(name=district_value)
       
        try:
            phone_number_value = "0" + str(int(phone_number_value))
            organization = Organization(
                        facility_name=facility_name_value.strip(),
                        phone_number=phone_number_value.strip(),
                        district=district_value,
                        latitude=latitude,
                        longitude=longitude
                        )
            organization.save()
        except Exception:
            print(traceback.print_exc())
