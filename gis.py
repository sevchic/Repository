import sqlalchemy as alch 
import cx_Oracle 
import requests
import json
import ast
import pandas
import warnings
import time
import re
from pprint import pprint, pformat
from setAccount1 import generation_Account, generation_MeteringDevice, generation_Contract, generation_MeteringDV, generation_ChargeDocument,generation_Payments, generation_AddrObjData, generation_HouseObjData, Generation_guid



with open('./conf/settings.json', 'r', encoding="utf-8-sig") as f:
    settings_json = json.loads(f.read())
type_of_test = settings_json['test_settings']['type_of_test']
load_json = settings_json['test_settings']['load_json']
username = settings_json['server']['gis_bd']['username']
password = settings_json['server']['gis_bd']['password']
service_name = settings_json['server']['gis_bd']['service_name']
ip = settings_json['server']['gis_bd']['ip']
servercfg = "oracle://"+username+":"+password+"@"+ip+"/?service_name="+service_name+""
rbd_engine = alch.create_engine(servercfg) 
rbd_conn = rbd_engine.connect()
warnings.filterwarnings("ignore")
file_error = open('./data/error.txt', 'w')

def setAccount():
    service = 'setAccount'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_LS0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setAccount_reconciliation(p_json)
            counter_f = counter_f+1
def setMeteringDevice():
    service = 'setMeteringDevice'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_PU0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setMeteringDevice_reconciliation(p_json)
            counter_f = counter_f+1
def setMeteringDeviceValues():
    service = 'setMeteringDeviceValues'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_PPU0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setMeteringDeviceValues_reconciliation(p_json)
            counter_f = counter_f+1
def setChargeDocument():
    service = 'setChargeDocument'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_PD0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setChargeDocument_reconciliation(p_json)
            counter_f = counter_f+1
def setAddrObjData():
    service = 'setAddrObjData'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_ADR0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setAddrObjData_reconciliation(p_json)
            counter_f = counter_f+1
def setHouseObjData():
    service = 'setHouseObjData'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_HO0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setAddrObjHouse_reconciliation(p_json)
            counter_f = counter_f+1
def setContract():
    service = 'setContract'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_DOG0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setContract_reconciliation(p_json)
            counter_f = counter_f+1    
def setPayments():
    service = 'setPayments'
    if type_of_test == 1 or type_of_test == 3:    

        name_test = 'Succ_file_PAY0001'
        error = 'CREATED'
        counter_f = 1
        file_count = settings_json['test_load_file'][''+service+'']['count_file']
        file_name = settings_json['test_load_file'][''+service+'']['file_name']
        if file_count == 0:
            return()
        while counter_f <= file_count:
            file_json_direct = './data/'+file_name+' ('+str(counter_f)+').json'
            file_json = read_json(file_json_direct)
            p_json,answer = f_load_json(file_json,service)
            #response_answer(answer,error,p_json,name_test)
            setPayments_reconciliation(p_json)
            counter_f = counter_f+1
# Получение данных из json и бд и их отправка в функцию сверки
# Входные данные: json
def setAccount_reconciliation(parsed_data): #Абоненты
    kol_account = (len(parsed_data['account']))-1 #Считаем сколько объектов в блоке account
    i=-1
    # Работаем с i аккаунтом
    while i < kol_account:
        i=i+1
        error = ''
        nm_org_uuid = str(parsed_data['info']['nm_org_uuid']) #Получаем uuid организации из json
        id_org = str(f_org(nm_org_uuid)) #Отправляем uuid организации в функцию и получаем ее id в базе
        value = pformat(parsed_data['account'][i]['id_account']) #Получаем id_account из json    
        count = f_count('g2_stg_account','id_account',value) #Отправляе id_account в функцию для подсчета колличества аккаунтов в таблице
        if count == 0: #Если аккаунтов в базе 0
            wright_txt('Абонент nm_account = '+value+' не найден')
        elif count > 1: #Если аккаунтов в базе больше 1
            wright_txt('Найдено абонентов больше 1 nm_account = '+value+'')
        else: #Если в базе 1 аккаунт
            g2_stg_account_mas = f_find_account(value) #Получаем все данные по аккаунту из базы
            #g2_stg_account_mas = generation_sql_select('G2_STG_ACCOUNT','id_account',id_account)


            if g2_stg_account_mas[0]['nm_error_code'] != None:
                wright_txt('абонеет id '+value+' загрузился с ошибкой. nm_error_code = '+str(g2_stg_account_mas[0]['nm_error_code']))
            else:

                #Расскладываем данные из json по переменным
                period = parsed_date_time(str(parsed_data['info']['dt_report_period']))
                nm_exch_key = (parsed_data['account'][i]['nm_exch_key'])
                dt_actual = parsed_date_time(str(parsed_data['account'][i]['dt_actual']))
                id_account = (parsed_data['account'][i]['id_account'])
                nm_account = (parsed_data['account'][i]['nm_account'])
                kd_open = (parsed_data['account'][i]['kd_open'])
                nn_living_people_number = (parsed_data['account'][i]['nn_living_people_number'])
                nn_total_area = ((str(parsed_data['account'][i]['nn_total_area'])).replace(',','.'))
                nn_residential_area = ((str(parsed_data['account'][i]['nn_residential_area'])).replace(',','.'))
                nn_heated_area = ((str(parsed_data['account'][i]['nn_heated_area'])).replace(',','.'))
                dt_close = parsed_date_time(str(parsed_data['account'][i]['dt_close']))
                id_closing_reason = (parsed_data['account'][i]['id_closing_reason'])
                nn_own_percent = (parsed_data['account'][i]['nn_own_percent'])
                nn_type_owner = (parsed_data['account'][i]['nn_type_owner'])
                nm_surname = (parsed_data['account'][i]['nm_surname'])
                nm_name = (parsed_data['account'][i]['nm_name'])
                nm_middle_name = (parsed_data['account'][i]['nm_middle_name'])
                nm_sex = (parsed_data['account'][i]['nm_sex'])
                dt_date_birth = parsed_date_time(str(parsed_data['account'][i]['dt_date_birth']))
                id_identity_document = (parsed_data['account'][i]['id_identity_document'])
                nm_serial_identity_document = (parsed_data['account'][i]['nm_serial_identity_document'])
                nm_number_identity_document = (parsed_data['account'][i]['nm_number_identity_document'])
                dt_identity_document = parsed_date_time(str(parsed_data['account'][i]['dt_identity_document']))
                nm_snils = (parsed_data['account'][i]['nm_snils'])
                nn_state_reg_number = (parsed_data['account'][i]['nn_state_reg_number'])
                kd_hold = (parsed_data['account'][i]['kd_hold'])
    

                #Расскладываем данные из бд по переменным
                nm_exch_key_t = str(g2_stg_account_mas[0]['nm_exch_key'])
                dt_actual_t = parsed_date_time(str(g2_stg_account_mas[0]['dt_actual']))
                nm_org_uuid_t = (g2_stg_account_mas[0]['nm_org_uuid'])
                id_account_t = (g2_stg_account_mas[0]['id_account'])
                nm_account_t = (g2_stg_account_mas[0]['nm_account'])
                kd_open_t = (g2_stg_account_mas[0]['kd_open'])
                nn_living_people_number_t = (g2_stg_account_mas[0]['nn_living_people_number'])
                nn_total_area_t = str(g2_stg_account_mas[0]['nn_total_area'])
                nn_residential_area_t = str(g2_stg_account_mas[0]['nn_residential_area'])
                nn_heated_area_t = str(g2_stg_account_mas[0]['nn_heated_area'])
                dt_close_t = parsed_date_time(str(g2_stg_account_mas[0]['dt_close']))
                id_close_reason_t = int(g2_stg_account_mas[0]['id_close_reason'])
                nn_own_percent_t = (g2_stg_account_mas[0]['nn_own_percent'])
                nn_type_owner_t = (g2_stg_account_mas[0]['nn_type_owner'])
                nm_surname_t = (g2_stg_account_mas[0]['nm_surname'])
                nm_name_t = (g2_stg_account_mas[0]['nm_name'])
                nm_middle_name_t = (g2_stg_account_mas[0]['nm_middle_name'])
                nm_sex_t = (g2_stg_account_mas[0]['nm_sex'])
                dt_date_birth_t = parsed_date_time(str(g2_stg_account_mas[0]['dt_date_birth']))
                id_identity_document_t = int(g2_stg_account_mas[0]['id_identity_document'])
                nm_serial_identity_document_t = (g2_stg_account_mas[0]['nm_serial_identity_document'])
                nm_number_identity_document_t = (g2_stg_account_mas[0]['nm_number_identity_document'])
                dt_identity_document_t = parsed_date_time(str(g2_stg_account_mas[0]['dt_identity_document']))
                nm_snils_t = (g2_stg_account_mas[0]['nm_snils'])
                nn_state_reg_number_t = (g2_stg_account_mas[0]['nn_state_reg_number'])
                kd_hold_t = (g2_stg_account_mas[0]['kd_hold'])
                nm_transport_uuid_t = (g2_stg_account_mas[0]['nm_transport_uuid'])
                nm_error_code_t = (g2_stg_account_mas[0]['nm_error_code'])
                nm_error_description_t = (g2_stg_account_mas[0]['nm_error_description'])
                load_id_t = (g2_stg_account_mas[0]['load_id'])
                is_valid_t = (g2_stg_account_mas[0]['is_valid'])
                    
                #Отправляем данные в функцию сверки
                function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. id_account = '+id_account+'')
                function_reconciliation(dt_actual_t,dt_actual,'dt_actual_t != dt_actual. id_account = '+id_account+'')
                function_reconciliation(id_account_t,id_account,'id_account_t != id_account. id_account = '+id_account+'')
                function_reconciliation(nm_account_t,nm_account,'nm_account_t != nm_account. id_account = '+id_account+'')
                function_reconciliation(nn_living_people_number_t,nn_living_people_number,'nn_living_people_number_t != nn_living_people_number. id_account = '+id_account+'')
                function_reconciliation(nn_total_area_t,nn_total_area,'nn_total_area_t != nn_total_area. id_account = '+id_account+'')
                function_reconciliation(nn_residential_area_t,nn_residential_area,'nn_residential_area_t != nn_residential_area. id_account = '+id_account+'')
                function_reconciliation(nn_heated_area_t,nn_heated_area,'nn_heated_area_t != nn_heated_area. id_account = '+id_account+'')
                function_reconciliation(id_close_reason_t,id_closing_reason,'id_close_reason_t != id_closing_reason. id_account = '+id_account+'')
                function_reconciliation(nn_own_percent_t,nn_own_percent,'nn_own_percent_t != nn_own_percent. id_account = '+id_account+'')
                function_reconciliation(nn_type_owner_t,nn_type_owner,'nn_type_owner_t != nn_type_owner. id_account = '+id_account+'')
                function_reconciliation(nm_surname_t,nm_surname,'nm_surname_t != nm_surname. id_account = '+id_account+'')
                function_reconciliation(nm_name_t,nm_name,'nm_name_t != nm_name. id_account = '+id_account+'')
                function_reconciliation(nm_middle_name_t,nm_middle_name,'nm_middle_name_t != nm_middle_name. id_account = '+id_account+'')
                function_reconciliation(nm_sex_t,nm_sex,'nm_sex_t != nm_sex. id_account = '+id_account+'')
                function_reconciliation(dt_date_birth_t,dt_date_birth,'dt_date_birth_t != dt_date_birth. id_account = '+id_account+'')
                function_reconciliation(id_identity_document_t,id_identity_document,'id_identity_document_t != id_identity_document. id_account = '+id_account+'')
                function_reconciliation(nm_serial_identity_document_t,nm_serial_identity_document,'nm_serial_identity_document_t != nm_serial_identity_document. id_account = '+id_account+'')
                function_reconciliation(nm_number_identity_document_t,nm_number_identity_document,'nm_number_identity_document_t != nm_number_identity_document. id_account = '+id_account+'')
                function_reconciliation(dt_identity_document_t,dt_identity_document,'dt_identity_document_t != dt_identity_document. id_account = '+id_account+'')
                function_reconciliation(nm_snils_t,nm_snils,'nm_snils_t != nm_snils. id_account = '+id_account+'')
                function_reconciliation(nn_state_reg_number_t,nn_state_reg_number,'nn_state_reg_number_t != nn_state_reg_number. id_account = '+id_account+'')
                function_reconciliation(kd_hold_t,kd_hold,'kd_hold_t != kd_hold. id_account = '+id_account+'')

                #Проверка наличия связи абонентов с договоров
                kol_contract = (len(parsed_data['account'][i]['contracts']))-1           
                if kol_contract >= 0:
                    i2=-1
                    # Работаем с i контрактом
                    while i2 < kol_contract:
                        i2=i2+1
                        id_contract = pformat(parsed_data['account'][i]['contracts'][i2]['id_contract'])
                        table = 'G2_STG_ACCOUNT_CONTRACT'
                        field_2 = 'ID_ACCOUNT'
                        field2_2 = 'ID_CONTRACT'
                        metering_device_account_count = f_count_2field(table,field_2,value,field2_2,id_contract)
                        if metering_device_account_count == 0:
                            wright_txt('Не создалась связь абонента со договором. ID_METERING_DEVIC: '+value+' ID_ACCOUNT: '+id_account+'')
def setAddrObjData_reconciliation(parsed_data_h): #Адреса
    kol_house = (len(parsed_data_h['address_object']))-1 #Считаем сколько объектов в блоке address_object
    i=-1
    # Работаем с i адресом
    while i < kol_house:
        Unicodeerror_h = 0
        i=i+1
        table = 'G2_STG_ADDRESS_OBJECT' #Название таблицы хранения адресов в бд 
        field = 'ID_FIAS_GUID' #Название поля (иникального индификатора) в базе для поиска адреса
        value = (pformat(parsed_data_h['address_object'][i]['id_fias_guid'])) #Получаем id_fias_guid из json
        count = f_count (table,field,value) #Отправляе id_fias_guid в функцию для подсчета колличества адресов в таблице
        if count == 0: #Если адресов в базе 0
            wright_txt(value+' '+'адресный объект не найден')
        elif count > 1: #Если адресов в базе больше 1
            wright_txt('объектов больше 1')
        else: #Если в базе 1 адрес
            g2_stg_address_object_table = rbd_conn.execute(""+generation_sql_select(table,field,value)+"")#Получаем все данные по адресу из базы
            try: #Проверка на ошибку в кодеровке данных
                g2_stg_address_object_mas = g2_stg_address_object_table.fetchall()
            except UnicodeDecodeError:
                wright_txt('ошибка в кодировке данных в g2_stg_address_object')
                Unicodeerror_h = 1
            if Unicodeerror_h == 1:
                return()

            if g2_stg_address_object_mas[0]['nm_error_code'] != None:
                wright_txt('адрес id_fias_guid', value, 'загрузился с ошибкой. nm_error_code =', str(g2_stg_address_object_mas[0]['nm_error_code']))
            else:

                #Расскладываем данные из json по переменным
                nm_exch_key = (parsed_data_h['address_object'][i]['nm_exch_key'])
                dt_actual = parsed_date_time(str(parsed_data_h['address_object'][i]['dt_actual']))
                nn_house_type = (parsed_data_h['address_object'][i]['nn_house_type'])
                id_fias_guid = (parsed_data_h['address_object'][i]['id_fias_guid'])
                nm_oktmo = (parsed_data_h['address_object'][i]['nm_oktmo'])
                kd_houses_same_address = (parsed_data_h['address_object'][i]['kd_houses_same_address'])
                nm_postcode = (parsed_data_h['address_object'][i]['nm_postcode'])
                nm_region = (parsed_data_h['address_object'][i]['nm_region'])
                nm_autonomic_region = (parsed_data_h['address_object'][i]['nm_autonomic_region'])
                nm_district = (parsed_data_h['address_object'][i]['nm_district'])
                nm_city = (parsed_data_h['address_object'][i]['nm_city'])
                nm_intracity_district = (parsed_data_h['address_object'][i]['nm_intracity_district'])
                nm_place = (parsed_data_h['address_object'][i]['nm_place'])
                nm_planning_structure = (parsed_data_h['address_object'][i]['nm_planning_structure'])
                nm_street = (parsed_data_h['address_object'][i]['nm_street'])
                nm_house_number = (parsed_data_h['address_object'][i]['nm_house_number'])
                nm_build_number = (parsed_data_h['address_object'][i]['nm_build_number'])
                nm_structure_number = (parsed_data_h['address_object'][i]['nm_structure_number'])

                #Расскладываем данные из бд по переменным
                nm_exch_key_t = (g2_stg_address_object_mas[0]['nm_exch_key'])
                dt_actual_t = parsed_date_time(str(g2_stg_address_object_mas[0]['dt_actual']))
                id_fias_guid_t = (g2_stg_address_object_mas[0]['id_fias_guid'])
                nn_house_type_t = (g2_stg_address_object_mas[0]['nn_house_type'])
                nm_oktmo_t = (g2_stg_address_object_mas[0]['nm_oktmo'])
                kd_houses_same_address_t = (g2_stg_address_object_mas[0]['kd_houses_same_address'])
                nm_postcode_t = (g2_stg_address_object_mas[0]['nm_postcode'])
                nm_region_t = (g2_stg_address_object_mas[0]['nm_region'])
                nm_autonomic_region_t = (g2_stg_address_object_mas[0]['nm_autonomic_region'])
                nm_district_t = (g2_stg_address_object_mas[0]['nm_district'])
                nm_city_t = (g2_stg_address_object_mas[0]['nm_city'])
                nm_intracity_district_t = (g2_stg_address_object_mas[0]['nm_intracity_district'])
                nm_place_t = (g2_stg_address_object_mas[0]['nm_place'])
                nm_planning_structure_t = (g2_stg_address_object_mas[0]['nm_planning_structure'])
                nm_street_t = (g2_stg_address_object_mas[0]['nm_street'])
                nm_house_number_t = (g2_stg_address_object_mas[0]['nm_house_number'])
                nm_build_number_t = (g2_stg_address_object_mas[0]['nm_build_number'])
                nm_structure_number_t = (g2_stg_address_object_mas[0]['nm_structure_number'])
                nm_transport_uuid_t = (g2_stg_address_object_mas[0]['nm_transport_uuid'])
                nm_error_code_t = (g2_stg_address_object_mas[0]['nm_error_code'])
                nm_error_description_t = (g2_stg_address_object_mas[0]['nm_error_description'])
                

                #Отправляем данные в функцию сверки
                function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. address_object id_fias_guid = '+value+'')
                function_reconciliation(dt_actual_t,dt_actual,'dt_actual_t != dt_actual. address_object id_fias_guid = '+value+'')
                function_reconciliation(id_fias_guid_t,id_fias_guid,'id_fias_guid_t != id_fias_guid. address_object id_fias_guid = '+value+'')
                function_reconciliation(nn_house_type_t,nn_house_type,'nn_house_type_t != nn_house_type. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_oktmo_t,nm_oktmo,'nm_oktmo_t != nm_oktmo. address_object id_fias_guid = '+value+'')
                function_reconciliation(kd_houses_same_address_t,kd_houses_same_address,'kd_houses_same_address_t != kd_houses_same_address. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_postcode_t,nm_postcode,'nm_postcode_t != nm_postcode. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_region_t,nm_region,'nm_region_t != nm_region. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_autonomic_region_t,nm_autonomic_region,'nm_autonomic_region_t != nm_autonomic_region. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_district_t,nm_district,'nm_district_t != nm_district. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_city_t,nm_city,'nm_city_t != nm_city. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_intracity_district_t,nm_intracity_district,'nm_intracity_district_t != nm_intracity_district. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_place_t,nm_place,'nm_place_t != nm_place. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_planning_structure_t,nm_planning_structure,'nm_planning_structure_t != nm_planning_structure. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_street_t,nm_street,'nm_street_t != nm_street. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_house_number_t,nm_house_number,'nm_house_number_t != nm_house_number. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_build_number_t,nm_build_number,'nm_build_number_t != nm_build_number. address_object id_fias_guid = '+value+'')
                function_reconciliation(nm_structure_number_t,nm_structure_number,'nm_structure_number_t != nm_structure_number. address_object id_fias_guid = '+value+'')
def setAddrObjHouse_reconciliation(parsed_data): #Дома
    kol_house = (len(parsed_data['house_object']))-1 #Считаем сколько объектов в блоке house_object
    i=-1
	# Работаем с i домом
    while i < kol_house:
        Unicodeerror_h = 0
        i=i+1
        table = 'G2_STG_HOUSE_OBJECT' #Название таблицы хранения домов в бд 
        field = 'ID_FIAS_GUID' #Название поля (иникального индификатора) в базе для поиска дома
        value = (pformat(parsed_data['house_object'][0]['id_fias_guid'])) #Получаем id_fias_guid из json
        count = f_count (table,field,value) #Отправляе id_fias_guid в функцию для подсчета колличества домов в таблице
        if count == 0: #Если домов в базе 0
            wright_txt(value+' '+'адресный объект не найден')
        elif count > 1: #Если домов в базе больше 1
            wright_txt('объектов больше 1')
        else: #Если в базе 1 дом
            g2_stg_house_object_table = rbd_conn.execute(""+generation_sql_select(table,field,value)+"")
            try: #Проверка на ошибку в кодеровке данных
                g2_stg_house_object_mas = g2_stg_house_object_table.fetchall()
            except UnicodeDecodeError:
                wright_txt('ошибка в кодировке данных в g2_stg_house_object')
                Unicodeerror_h = 1
            if Unicodeerror_h == 1:
                return()


            if g2_stg_house_object_mas[0]['nm_error_code'] != None:
                wright_txt('дом id_fias_guid', value, 'загрузился с ошибкой. nm_error_code =', str(g2_stg_house_object_mas[0]['nm_error_code']))
            else:

                #Расскладываем данные из json по переменным
                nm_exch_key = (parsed_data['house_object'][i]['nm_exch_key'])
                id_house_object = (parsed_data['house_object'][i]['id_house_object'])
                id_fias_guid = (parsed_data['house_object'][i]['id_fias_guid'])
                dt_actual = parsed_date_time(str(parsed_data['house_object'][i]['dt_actual']))
                nn_type_object = (parsed_data['house_object'][i]['nn_type_object'])
                id_fias_guid_parent = (parsed_data['house_object'][i]['id_fias_guid_parent'])
                nm_entrance = (parsed_data['house_object'][i]['nm_entrance'])
                nm_block = (parsed_data['house_object'][i]['nm_block'])
                nm_premises = (parsed_data['house_object'][i]['nm_premises'])
                nm_room = (parsed_data['house_object'][i]['nm_room'])
                nn_total_area = (parsed_data['house_object'][i]['nn_total_area'])
                id_reasons_cancell =(parsed_data['house_object'][i]['id_reasons_cancell'])
                nm_address_full =(parsed_data['house_object'][i]['nm_address_full'])

                #Расскладываем данные из бд по переменным
                nm_org_uuid_t = (g2_stg_house_object_mas[0]['nm_org_uuid'])
                id_contract_t = (g2_stg_house_object_mas[0]['id_contract'])
                id_account_t = (g2_stg_house_object_mas[0]['id_account'])
                id_metering_device_t = (g2_stg_house_object_mas[0]['id_metering_device'])
                id_fias_guid_t = (g2_stg_house_object_mas[0]['id_fias_guid'])
                id_fias_guid_parent_t = (g2_stg_house_object_mas[0]['id_fias_guid_parent'])
                nn_house_object_type_t = (g2_stg_house_object_mas[0]['nn_house_object_type'])
                nm_entrance_t = (g2_stg_house_object_mas[0]['nm_entrance'])
                nm_premises_t = (g2_stg_house_object_mas[0]['nm_premises'])
                nm_block_t = (g2_stg_house_object_mas[0]['nm_block'])
                nm_room_t = (g2_stg_house_object_mas[0]['nm_room'])
                nn_total_area_t = (g2_stg_house_object_mas[0]['nn_total_area'])
                id_reasons_cancel_t = (g2_stg_house_object_mas[0]['id_reasons_cancel'])
                nm_entrance_transport_uuid_t = (g2_stg_house_object_mas[0]['nm_entrance_transport_uuid'])
                nm_premises_transport_uuid_t = (g2_stg_house_object_mas[0]['nm_premises_transport_uuid'])
                nm_block_transport_uuid_t = (g2_stg_house_object_mas[0]['nm_block_transport_uuid'])
                nm_room_transport_uuid_t = (g2_stg_house_object_mas[0]['nm_room_transport_uuid'])
                nm_exch_key_t = (g2_stg_house_object_mas[0]['nm_exch_key'])
                dt_actual_t = parsed_date_time(str(g2_stg_house_object_mas[0]['dt_actual']))
                id_house_object_t = (g2_stg_house_object_mas[0]['id_house_object'])
                nm_error_code_t = (g2_stg_house_object_mas[0]['nm_error_code'])
                nm_error_description_t = (g2_stg_house_object_mas[0]['nm_error_description'])
                nm_address_full_t = (g2_stg_house_object_mas[0]['nm_address_full'])

                #Отправляем данные в функцию сверки
                function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. house_object - id_fias_guid = '+value+'')
                function_reconciliation(id_house_object_t,id_house_object,'id_house_object_t != id_house_object. house_object - id_fias_guid = '+value+'')
                function_reconciliation(id_fias_guid_t,id_fias_guid,'id_fias_guid_t != id_fias_guid. house_object - id_fias_guid = '+value+'')
                function_reconciliation(dt_actual_t,dt_actual,'dt_actual_t != dt_actual. house_object - id_fias_guid = '+value+'')
                function_reconciliation(id_fias_guid_parent_t,id_fias_guid_parent,'id_fias_guid_parent_t != id_fias_guid_parent. house_object - id_fias_guid = '+value+'')
                function_reconciliation(nm_entrance_t,nm_entrance,'nm_entrance_t != nm_entrance. house_object - id_fias_guid = '+value+'')
                function_reconciliation(nm_block_t,nm_block,'nm_block_t != nm_block. house_object - id_fias_guid = '+value+'')
                function_reconciliation(nm_premises_t,nm_premises,'nm_premises_t != nm_premises. house_object - id_fias_guid = '+value+'')
                function_reconciliation(nm_room_t,nm_room,'nm_room_t != nm_room. house_object - id_fias_guid = '+value+'')
                function_reconciliation(nn_total_area_t,nn_total_area,'nn_total_area_t != nn_total_area. house_object - id_fias_guid = '+value+'')
                function_reconciliation(nm_address_full_t,nm_address_full,'nm_address_full_t != nm_address_full. house_object - id_fias_guid = '+value+'')
def setPayments_reconciliation(parsed_data):  #Платежи 
    Unicodeerror_h = 0
    kol_payments = (len(parsed_data['payments']))-1 #Считаем сколько объектов в блоке payments
    i=-1
	# Работаем с i платежом
    while i < kol_payments:
        i=i+1
        error = ''
        table = 'G2_STG_PAYMENT' #Название таблицы хранения платежей в бд
        field = 'ID_PAYMENT' #Название поля (иникального индификатора) в базе для поиска платеж
        nm_org_uuid = str(parsed_data['info']['nm_org_uuid']) #Получаем nm_org_uuid из json
        id_org = str(f_org(nm_org_uuid)) #Получаем id организации в базе
        value = pformat(parsed_data['payments'][i]['id_payment']) #Получаем id_payment из json    
        count = f_count (table,field,value) #Отправляе id_payment в функцию для подсчета колличества домов в таблице
        if count == 0: #Если платежей в базе 0
            wright_txt('Платеж id_payment = '+value+' не найден')
        elif count > 1: #Если платежей в базе больше 1
            wright_txt('Найдено платежей больше 1 id_payment = '+value+'')
        else: #Если в базе 1 платеж
            g2_stg_payment_table = rbd_conn.execute(""+generation_sql_select(table,field,value)+"")
            try: #Проверка на ошибку в кодеровке данных
                g2_stg_payment_mas = g2_stg_payment_table.fetchall()
            except UnicodeDecodeError:
                wright_txt('ошибка в кодировке данных в g2_stg_payment_table')
                Unicodeerror_h = 1
            if Unicodeerror_h == 1:
                return()

            if g2_stg_payment_mas[0]['nm_error_code'] != None:
                wright_txt('платеж id_payment', value, 'загрузился с ошибкой. nm_error_code =', str(g2_stg_payment_mas[0]['nm_error_code']))
            else:
            
                #Расскладываем данные из json по переменным
                nm_exch_key = (parsed_data['payments'][i]['nm_exch_key'])
                id_payment = (parsed_data['payments'][i]['id_payment'])
                id_account = (parsed_data['payments'][i]['id_account'])
                nm_account = (parsed_data['payments'][i]['nm_account'])
                kd_correct = (parsed_data['payments'][i]['kd_correct'])
                kd_cancel = (parsed_data['payments'][i]['kd_cancel'])
                dt_pay = parsed_date_time(str(parsed_data['payments'][0]['dt_pay']))
                dt_period = parsed_date_time(str(parsed_data['payments'][0]['dt_period']))
                id_ipd = (parsed_data['payments'][i]['id_ipd'])
                id_zhku = (parsed_data['payments'][i]['id_zhku'])
                nn_sm_pay = float(parsed_data['payments'][i]['nn_sm_pay'])
                dt_pay_cancel = parsed_date_time(str(parsed_data['payments'][0]['dt_pay_cancel']))
                
                #Расскладываем данные из бд по переменным
                nm_org_uuid_t = (g2_stg_payment_mas[0]['nm_org_uuid'])
                id_payment_t = (g2_stg_payment_mas[0]['id_payment'])
                id_account_t = (g2_stg_payment_mas[0]['id_account'])
                nm_account_t = (g2_stg_payment_mas[0]['nm_account'])
                kd_correct_t = (g2_stg_payment_mas[0]['kd_correct'])
                kd_cancel_t = (g2_stg_payment_mas[0]['kd_cancel'])
                dt_pay_t = parsed_date_time(str(g2_stg_payment_mas[0]['dt_pay']))
                dt_period_t = parsed_date_time(str(g2_stg_payment_mas[0]['dt_period']))
                nn_sm_pay_t = float(g2_stg_payment_mas[0]['nn_sm_pay'])
                id_ipd_t = (g2_stg_payment_mas[0]['id_ipd'])
                id_zhku_t = (g2_stg_payment_mas[0]['id_zhku'])
                dt_pay_cancel_t = parsed_date_time(str(g2_stg_payment_mas[0]['dt_pay_cancel']))
                nm_exch_key_t = (g2_stg_payment_mas[0]['nm_exch_key'])
                nm_transport_uuid_t = (g2_stg_payment_mas[0]['nm_transport_uuid'])
                nm_error_code_t = (g2_stg_payment_mas[0]['nm_error_code'])
                nm_error_description_t = (g2_stg_payment_mas[0]['nm_error_description'])
    
                #Проверка информации
                function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. id_payment = '+value+'')
                function_reconciliation(id_payment_t,id_payment,'id_payment_t != id_payment. id_payment = '+value+'')
                function_reconciliation(id_account_t,id_account,'id_account_t != id_account. id_payment = '+value+'') 
                function_reconciliation(nm_account_t,nm_account,'nm_account_t != nm_account. id_payment = '+value+'') 
                function_reconciliation(kd_correct_t,kd_correct,'kd_correct_t != kd_correct. id_payment = '+value+'')   
                function_reconciliation(kd_cancel_t,kd_cancel,'kd_cancel_t != kd_cancel. id_payment = '+value+'')   
                function_reconciliation(dt_pay_t,dt_pay,'dt_pay_t != dt_pay. id_payment = '+value+'')   
                function_reconciliation(dt_period_t,dt_period,'dt_period_t != dt_period. id_payment = '+value+'')   
                function_reconciliation(id_ipd_t,id_ipd,'id_ipd_t != id_ipd. id_payment = '+value+'')   
                function_reconciliation(id_zhku_t,id_zhku,'id_zhku_t != id_zhku. id_payment = '+value+'')   
                function_reconciliation(nn_sm_pay_t,nn_sm_pay,'nn_sm_pay_t != nn_sm_pay. id_payment = '+value+'')   
                function_reconciliation(dt_pay_cancel_t,dt_pay_cancel,'dt_pay_cancel_t != dt_pay_cancel. id_payment = '+value+'')     
def setChargeDocument_reconciliation(parsed_data):  #Начисления 
    Unicodeerror_h = 0
    kol_charge_document = (len(parsed_data['charge_document']))-1 #Считаем сколько объектов в блоке charge_document
    i=-1
	# Работаем с i начислением
    while i < kol_charge_document:
        i=i+1

        table = 'G2_STG_CHARGE_DOCUMENT' #Название таблицы хранения начислений в бд 
        field = 'ID_CHARGE_DOCUMENT' #Название поля (иникального индификатора) в базе для поиска начислений
        field2 = 'NM_SERVICE_CODE' #Название поля (код услуги) в базе для поиска начислений
        value = pformat(parsed_data['charge_document'][i]['id_charge_document']) #Получаем id_charge_document из json  
        kol_charge_info = (len(parsed_data['charge_document'][i]['charge_info']))
        ici = 0
        kol_charge = 0
        while ici < kol_charge_info:
            kol_charge = kol_charge + (len(parsed_data['charge_document'][i]['charge_info'][ici]['charge'])) 
            ici = ici +1

        count = f_count(table,field,value)#Отправляем id_fias_guid в функцию для подсчета колличества начислений в таблице
        if count == 0: #Если начислений в базе 0
            wright_txt('Начисление id_charge_document = '+value+' не найдено')
        elif count != kol_charge: #Если начислений в базе не равно в jsone
            wright_txt('Начислений в базе не равно в jsone. id_charge_document = '+value+'')
        else: #Если в базе начисления равны в jsone
            ici2 = 0
            while ici2 < kol_charge_info:
                ic = 0
                kol_charge2 = (len(parsed_data['charge_document'][i]['charge_info'][ici2]['charge']))
                while ic < kol_charge2:
                    value2 = parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nm_service_code']
                    g2_stg_charge_document_table = rbd_conn.execute(""+generation_sql_select_2field(table,field,value,field2,value2)+"")
                    try: #Проверка на ошибку в кодеровке данных
                        g2_stg_charge_document_mas = g2_stg_charge_document_table.fetchall()
                    except UnicodeDecodeError:
                        wright_txt('ошибка в кодировке данных в g2_stg_payment_table')
                        Unicodeerror_h = 1
                    if Unicodeerror_h == 1:
                        return()
                    
                    if g2_stg_charge_document_mas[0]['nm_error_code'] != None:
                        wright_txt('начисление id_charge_document', value, 'загрузился с ошибкой. nm_error_code =', str(g2_stg_charge_document_mas[0]['nm_error_code']))
                    else:
                        #Расскладываем данные из json по переменным
                        nm_org_uuid = str(parsed_data['info']['nm_org_uuid'])
                        nm_exch_key = (parsed_data['charge_document'][i]['nm_exch_key'])
                        dt_actual = parsed_date_time(str(parsed_data['charge_document'][i]['dt_actual']))
                        id_charge_document = (parsed_data['charge_document'][i]['id_charge_document'])
                        id_account = (parsed_data['charge_document'][i]['id_account'])
                        nm_account = (parsed_data['charge_document'][i]['nm_account'])
                        id_charge_document_correct = (parsed_data['charge_document'][i]['id_charge_document_correct'])
                        dt_charge = parsed_date_time(str(parsed_data['charge_document'][i]['dt_charge']))
                        nn_debt_previous = (parsed_data['charge_document'][i]['nn_debt_previous'])
                        nn_advance_previous = (parsed_data['charge_document'][i]['nn_advance_previous'])
                        nn_total_sum = (parsed_data['charge_document'][i]['nn_total_sum'])
                        nn_total_sum_pd = (parsed_data['charge_document'][i]['nn_total_sum_pd'])
                        nn_pay_till = (parsed_data['charge_document'][i]['nn_pay_till'])
                        nn_pay_enter = (parsed_data['charge_document'][i]['nn_pay_enter'])
                        dt_pay_enter = parsed_date_time(str(parsed_data['charge_document'][i]['dt_pay_enter']))
                        nm_org_pu_uuid = (parsed_data['charge_document'][i]['charge_info'][ici2]['nm_org_pu_uuid'])
                        nm_bank_bik = (parsed_data['charge_document'][i]['charge_info'][ici2]['nm_bank_bik'])
                        nm_operating_account_number = (parsed_data['charge_document'][i]['charge_info'][ici2]['nm_operating_account_number'])
                        nm_service_code = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nm_service_code'])
                        nn_service_type = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_service_type'])
                        nn_tariff = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_tariff'])
                        nm_norm = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nm_norm'])
                        id_unit = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['id_unit'])
                        nn_volume_individ = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_volume_individ'])
                        nn_volume_odn = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_volume_odn'])
                        nn_boost_coef = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_boost_coef'])
                        nn_boost_coef_limit = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_boost_coef_limit'])
                        nn_total_accrued = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_total_accrued'])
                        nn_sum_privilege = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_sum_privilege'])
                        nn_sum_corr = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_sum_corr'])
                        nm_info_corr = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nm_info_corr'])
                        nn_rate_installment = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_rate_installment'])
                        nn_sum_installment = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_sum_installment'])
                        nn_sum_pay_with_installment_rate = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_sum_pay_with_installment_rate'])
                        nn_total_pay = (parsed_data['charge_document'][i]['charge_info'][ici2]['charge'][ic]['nn_total_pay'])

                        #Расскладываем данные из бд по переменным
                        nm_org_uuid_t = (g2_stg_charge_document_mas[0]['nm_org_uuid'])
                        id_charge_document_t = (g2_stg_charge_document_mas[0]['id_charge_document'])
                        id_account_t = (g2_stg_charge_document_mas[0]['id_account'])
                        dt_charge_t = parsed_date_time(str(g2_stg_charge_document_mas[0]['dt_charge']))
                        id_charge_document_correct_t = (g2_stg_charge_document_mas[0]['id_charge_document_correct'])
                        nn_debt_previous_t = (g2_stg_charge_document_mas[0]['nn_debt_previous'])
                        nn_advance_previous_t = (g2_stg_charge_document_mas[0]['nn_advance_previous'])
                        nn_total_sum_t = (g2_stg_charge_document_mas[0]['nn_total_sum'])
                        nn_total_sum_pd_t = (g2_stg_charge_document_mas[0]['nn_total_sum_pd'])
                        nn_pay_till_t = (g2_stg_charge_document_mas[0]['nn_pay_till'])
                        nn_pay_enter_t = (g2_stg_charge_document_mas[0]['nn_pay_enter'])
                        dt_pay_enter_t = parsed_date_time(str(g2_stg_charge_document_mas[0]['dt_pay_enter']))
                        nn_service_type_t = (g2_stg_charge_document_mas[0]['nn_service_type'])
                        nm_service_code_t = (g2_stg_charge_document_mas[0]['nm_service_code'])
                        nn_tariff_t = (g2_stg_charge_document_mas[0]['nn_tariff'])
                        nn_consumption_norm_t = (g2_stg_charge_document_mas[0]['nn_consumption_norm'])
                        nm_unit_t = (g2_stg_charge_document_mas[0]['nm_unit'])
                        nn_volume_individ_t = (g2_stg_charge_document_mas[0]['nn_volume_individ'])
                        nn_volume_odn_t = (g2_stg_charge_document_mas[0]['nn_volume_odn'])
                        nn_boost_coef_t = (g2_stg_charge_document_mas[0]['nn_boost_coef'])
                        nn_boost_coef_limit_t = (g2_stg_charge_document_mas[0]['nn_boost_coef_limit'])
                        nn_total_accrued_t = (g2_stg_charge_document_mas[0]['nn_total_accrued'])
                        nn_sum_privilege_t = (g2_stg_charge_document_mas[0]['nn_sum_privilege'])
                        nn_sum_corr_t = (g2_stg_charge_document_mas[0]['nn_sum_corr'])
                        nm_info_corr_t = (g2_stg_charge_document_mas[0]['nm_info_corr'])
                        nn_rate_installment_t = (g2_stg_charge_document_mas[0]['nn_rate_installment'])
                        nn_sum_installment_t = (g2_stg_charge_document_mas[0]['nn_sum_installment'])
                        nn_sum_pay_with_installment_rate_t = (g2_stg_charge_document_mas[0]['nn_sum_pay_with_installment_rate'])
                        nn_total_pay_t = (g2_stg_charge_document_mas[0]['nn_total_pay'])
                        nm_bank_bik_t = (g2_stg_charge_document_mas[0]['nm_bank_bik'])
                        nm_operating_account_number_t = (g2_stg_charge_document_mas[0]['nm_operating_account_number'])
                        nm_exch_key_t = (g2_stg_charge_document_mas[0]['nm_exch_key'])
                        dt_actual_t = parsed_date_time(str(g2_stg_charge_document_mas[0]['dt_actual']))
                        nm_transport_uuid_t = (g2_stg_charge_document_mas[0]['nm_transport_uuid'])
                        nm_error_code_t = (g2_stg_charge_document_mas[0]['nm_error_code'])
                        nm_error_description_t = (g2_stg_charge_document_mas[0]['nm_error_description'])
            
                        #Отправляем данные в функцию сверки
                        function_reconciliation(id_charge_document_t,id_charge_document,'id_charge_document_t != id_charge_document. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(id_account_t,id_account,'id_account_t != id_account. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(dt_charge_t,dt_charge,'dt_charge_t != dt_charge. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(id_charge_document_correct_t,id_charge_document_correct,'id_charge_document_correct_t != id_charge_document_correct. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_debt_previous_t,nn_debt_previous,'nn_debt_previous_t != nn_debt_previous. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_advance_previous_t,nn_advance_previous,'nn_advance_previous_t != nn_advance_previous. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_total_sum_t,nn_total_sum,'nn_total_sum_t != nn_total_sum. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_total_sum_pd_t,nn_total_sum_pd,'nn_total_sum_pd_t != nn_total_sum_pd. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_pay_till_t,nn_pay_till,'nn_pay_till_t != nn_pay_till. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_pay_enter_t,nn_pay_enter,'nn_pay_enter_t != nn_pay_enter. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(dt_pay_enter_t,dt_pay_enter,'dt_pay_enter_t != dt_pay_enter. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_service_type_t,nn_service_type,'nn_service_type_t != nn_service_type. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nm_service_code_t,nm_service_code,'nm_service_code_t != nm_service_code. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_tariff_t,nn_tariff,'nn_tariff_t != nn_tariff. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_consumption_norm_t,nm_norm,'nn_consumption_norm_t != nm_norm. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_volume_individ_t,nn_volume_individ,'nn_volume_individ_t != nn_volume_individ. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_volume_odn_t,nn_volume_odn,'nn_volume_odn_t != nn_volume_odn. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_boost_coef_t,nn_boost_coef,'nn_boost_coef_t != nn_boost_coef. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_boost_coef_limit_t,nn_boost_coef_limit,'nn_boost_coef_limit_t != nn_boost_coef_limit. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_total_accrued_t,nn_total_accrued,'nn_total_accrued_t != nn_total_accrued. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_sum_privilege_t,nn_sum_privilege,'nn_sum_privilege_t != nn_sum_privilege. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_sum_corr_t,nn_sum_corr,'nn_sum_corr_t != nn_sum_corr. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nm_info_corr_t,nm_info_corr,'nm_info_corr_t != nm_info_corr. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_rate_installment_t,nn_rate_installment,'nn_rate_installment_t != nn_rate_installment. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_sum_installment_t,nn_sum_installment,'nn_sum_installment_t != nn_sum_installment. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_sum_pay_with_installment_rate_t,nn_sum_pay_with_installment_rate,'nn_sum_pay_with_installment_rate_t != nn_sum_pay_with_installment_rate. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nn_total_pay_t,nn_total_pay,'nn_total_pay_t != nn_total_pay. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nm_bank_bik_t,nm_bank_bik,'nm_bank_bik_t != nm_bank_bik. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nm_operating_account_number_t,nm_operating_account_number,'nm_operating_account_number_t != nm_operating_account_number. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. id_charge_document = '+value+' nm_service_code = '+value2+'')
                        function_reconciliation(dt_actual_t,dt_actual,'dt_actual_t != dt_actual. id_charge_document = '+value+' nm_service_code = '+value2+'') 
                    
                    ic = ic+1
                ici2 = ici2+1
def setMeteringDevice_reconciliation(parsed_data):  #Приборы учета 
    Unicodeerror_h = 0
    kol_Meterin = (len(parsed_data['metering_device']))-1 #Считаем сколько объектов в блоке metering_device
    i=-1
    # Работаем с i прибором
    while i < kol_Meterin:
        i=i+1
        error = ''
        table = 'G2_STG_METERING_DEVICE' #Название таблицы хранения приборов учета в бд 
        field = 'ID_METERING_DEVICE' #Название поля (иникального индификатора) в базе для поиска прибора учета
        nm_org_uuid = str(parsed_data['info']['nm_org_uuid']) #Получаем nm_org_uuid организации из json
        id_org = str(f_org(nm_org_uuid)) #Получаем id организации из бд
        value = pformat(parsed_data['metering_device'][i]['id_metering_device'])     
        count = f_count(table,field,value) #Отправляем id_metering_device в функцию для подсчета колличества приборов в таблице
        if count == 0: #Если приборов в базе 0
            wright_txt('Счетчик id_metering_device = '+value+' не найден')
        elif count > 1: #Если приборов в базе больше 1
            wright_txt('Найдено счетчиков больше 1 id_metering_device = '+value+'')
        else: #Если в базе 1 прибор
            g2_stg_metering_device_table = rbd_conn.execute(""+generation_sql_select(table,field,value)+"")
            try: #Проверка на ошибку в кодеровке данных
                g2_stg_metering_device_mas = g2_stg_metering_device_table.fetchall()
            except UnicodeDecodeError:
                wright_txt('ошибка в кодировке данных в g2_stg_payment_table')
                Unicodeerror_h = 1
            if Unicodeerror_h == 1:
                return()

            if g2_stg_metering_device_mas[0]['nm_error_code'] != None:
                wright_txt('счетчик id_metering_device', value, 'загрузился с ошибкой. nm_error_code =', str(g2_stg_metering_device_mas[0]['nm_error_code']))
            else:

                #Расскладываем данные из json по переменным
                nm_exch_key = (parsed_data['metering_device'][i]['nm_exch_key'])
                dt_actual = parsed_date_time(str(parsed_data['metering_device'][i]['dt_actual']))
                id_metering_device = (parsed_data['metering_device'][i]['id_metering_device'])
                kd_status = (parsed_data['metering_device'][i]['kd_status'])
                nn_type_meter = (parsed_data['metering_device'][i]['nn_type_meter'])
                nm_serial_number = (parsed_data['metering_device'][i]['nm_serial_number'])
                nm_marka = (parsed_data['metering_device'][i]['nm_marka'])
                nm_model = (parsed_data['metering_device'][i]['nm_model'])
                dt_installation = parsed_date_time(str(parsed_data['metering_device'][i]['dt_installation']))
                dt_commissioned = parsed_date_time(str(parsed_data['metering_device'][i]['dt_commissioned']))
                kd_remote_measuring = (parsed_data['metering_device'][i]['kd_remote_measuring'])
                nm_remote_system = (parsed_data['metering_device'][i]['nm_remote_system'])
                dt_first_verification = parsed_date_time(str(parsed_data['metering_device'][i]['dt_first_verification']))
                id_verification_interval = (parsed_data['metering_device'][i]['id_verification_interval'])
                dt_seal = parsed_date_time(str(parsed_data['metering_device'][i]['dt_seal']))
                kd_temperature_sensor = (parsed_data['metering_device'][i]['kd_temperature_sensor'])
                nm_temperature_sensor_info = (parsed_data['metering_device'][i]['nm_temperature_sensor_info'])
                kd_pressure_sensor = (parsed_data['metering_device'][i]['kd_pressure_sensor'])
                nm_pressure_sensor_info = (parsed_data['metering_device'][i]['nm_pressure_sensor_info'])
                kd_consumed_volume = (parsed_data['metering_device'][i]['kd_consumed_volume'])
                id_municipal_resource_type = (parsed_data['metering_device'][i]['id_municipal_resource_type'])
                id_unit = (parsed_data['metering_device'][i]['id_unit'])
                nn_connection_type = (parsed_data['metering_device'][i]['nn_connection_type'])
                nn_tariff = (parsed_data['metering_device'][i]['nn_tarif'])
                nn_value_1 = (parsed_data['metering_device'][i]['nn_value_1'])
                nn_value_arhive_1 = (parsed_data['metering_device'][i]['nn_value_arhive_1'])
                nn_value_2 = (parsed_data['metering_device'][i]['nn_value_2'])
                nn_value_arhive_2 = (parsed_data['metering_device'][i]['nn_value_arhive_2'])
                nn_value_3 = (parsed_data['metering_device'][i]['nn_value_3'])
                nn_value_arhive_3 = (parsed_data['metering_device'][i]['nn_value_arhive_3'])
                nn_transformation_ratio = (parsed_data['metering_device'][i]['nn_transformation_ratio'])
                nn_archiving_type = (parsed_data['metering_device'][i]['nn_archiving_type'])
                id_reason_archiving = (parsed_data['metering_device'][i]['id_archiving_reason'])
                kd_planned_verification = (parsed_data['metering_device'][i]['kd_planned_verification'])
                id_failure_reason = (parsed_data['metering_device'][i]['id_failure_reason'])
                id_metering_device_replace = (parsed_data['metering_device'][i]['id_metering_device_replace'])
                
                #Расскладываем данные из бд по переменным
                nm_exch_key_t = (g2_stg_metering_device_mas[0]['nm_exch_key'])
                dt_actual_t = parsed_date_time(str(g2_stg_metering_device_mas[0]['dt_actual']))
                nm_org_uuid_t = (g2_stg_metering_device_mas[0]['nm_org_uuid'])
                id_metering_device_t = (g2_stg_metering_device_mas[0]['id_metering_device'])
                kd_status_t = (g2_stg_metering_device_mas[0]['kd_status'])
                nn_type_meter_t = (g2_stg_metering_device_mas[0]['nn_type_meter'])
                nm_serial_number_t = (g2_stg_metering_device_mas[0]['nm_serial_number'])
                nm_marka_t = (g2_stg_metering_device_mas[0]['nm_marka'])
                nm_model_t = (g2_stg_metering_device_mas[0]['nm_model'])
                dt_installation_t = parsed_date_time(str(g2_stg_metering_device_mas[0]['dt_installation']))
                dt_commissioned_t = parsed_date_time(str(g2_stg_metering_device_mas[0]['dt_commissioned']))
                kd_remote_measuring_t = (g2_stg_metering_device_mas[0]['kd_remote_measuring'])
                nm_remote_system_t = (g2_stg_metering_device_mas[0]['nm_remote_system'])
                dt_first_verification_t = parsed_date_time(str(g2_stg_metering_device_mas[0]['dt_first_verification']))
                id_verification_interval_t = (g2_stg_metering_device_mas[0]['id_verification_interval'])
                dt_seal_t = parsed_date_time(str(g2_stg_metering_device_mas[0]['dt_seal']))
                kd_temperature_sensor_t = (g2_stg_metering_device_mas[0]['kd_temperature_sensor'])
                nm_temperature_sensor_info_t = (g2_stg_metering_device_mas[0]['nm_temperature_sensor_info'])
                kd_pressure_sensor_t = (g2_stg_metering_device_mas[0]['kd_pressure_sensor'])
                nm_pressure_sensor_info_t = (g2_stg_metering_device_mas[0]['nm_pressure_sensor_info'])
                kd_consumed_volume_t = (g2_stg_metering_device_mas[0]['kd_consumed_volume'])
                id_municipal_resource_type_t = (g2_stg_metering_device_mas[0]['id_municipal_resource_type'])
                nn_connection_type_t = (g2_stg_metering_device_mas[0]['nn_connection_type'])
                nn_tariff_t = (g2_stg_metering_device_mas[0]['nn_tariff'])
                nn_value_1_t = (g2_stg_metering_device_mas[0]['nn_value_1'])
                nn_value_arhive_1_t = (g2_stg_metering_device_mas[0]['nn_value_arhive_1'])
                nn_value_2_t = (g2_stg_metering_device_mas[0]['nn_value_2'])
                nn_value_arhive_2_t = (g2_stg_metering_device_mas[0]['nn_value_arhive_2'])
                nn_value_3_t = (g2_stg_metering_device_mas[0]['nn_value_3'])
                nn_value_arhive_3_t = (g2_stg_metering_device_mas[0]['nn_value_arhive_3'])
                nn_transformation_ratio_t = (g2_stg_metering_device_mas[0]['nn_transformation_ratio'])
                id_linked_metering_device_list_t = (g2_stg_metering_device_mas[0]['id_linked_metering_device_list'])
                nn_archiving_type_t = (g2_stg_metering_device_mas[0]['nn_archiving_type'])
                id_reason_archiving_t = (g2_stg_metering_device_mas[0]['id_reason_archiving'])
                kd_planned_verification_t = (g2_stg_metering_device_mas[0]['kd_planned_verification'])
                id_reason_fail_t = (g2_stg_metering_device_mas[0]['id_reason_fail'])
                id_metering_device_replace_t = (g2_stg_metering_device_mas[0]['id_metering_device_replace'])
                nm_transport_uuid_t = (g2_stg_metering_device_mas[0]['nm_transport_uuid'])
                id_unit_t = (g2_stg_metering_device_mas[0]['id_unit'])
    
                #Отправляем данные в функцию сверки
                function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. id_metering_device = '+id_metering_device+'')
                function_reconciliation(dt_actual_t,dt_actual,'dt_actual_t != dt_actual. id_metering_device = '+id_metering_device+'')
                function_reconciliation(id_metering_device_t,id_metering_device,'id_metering_device_t != id_metering_device. id_metering_device = '+id_metering_device+'')
                function_reconciliation(kd_status_t,kd_status,'kd_status_t != kd_status. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_type_meter_t,nn_type_meter,'nn_type_meter_t != nn_type_meter. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nm_serial_number_t,nm_serial_number,'nm_serial_number_t != nm_serial_number. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nm_marka_t,nm_marka,'nm_marka_t != nm_marka. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nm_model_t,nm_model,'nm_model_t != nm_model. id_metering_device = '+id_metering_device+'')
                function_reconciliation(dt_installation_t,dt_installation,'dt_installation_t != dt_installation. id_metering_device = '+id_metering_device+'')
                function_reconciliation(dt_commissioned_t,dt_commissioned,'dt_commissioned_t != dt_commissioned. id_metering_device = '+id_metering_device+'')
                function_reconciliation(kd_remote_measuring_t,kd_remote_measuring,'kd_remote_measuring_t != kd_remote_measuring. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nm_remote_system_t,nm_remote_system,'nm_remote_system_t != nm_remote_system. id_metering_device = '+id_metering_device+'')
                function_reconciliation(dt_first_verification_t,dt_first_verification,'dt_first_verification_t != dt_first_verification. id_metering_device = '+id_metering_device+'')
                function_reconciliation(id_verification_interval_t,id_verification_interval,'id_verification_interval_t != id_verification_interval. id_metering_device = '+id_metering_device+'')
                function_reconciliation(dt_seal_t,dt_seal,'dt_seal_t != dt_seal. id_metering_device = '+id_metering_device+'')
                function_reconciliation(kd_temperature_sensor_t,kd_temperature_sensor,'kd_temperature_sensor_t != kd_temperature_sensor. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nm_temperature_sensor_info_t,nm_temperature_sensor_info,'nm_temperature_sensor_info_t != nm_temperature_sensor_info. id_metering_device = '+id_metering_device+'')
                function_reconciliation(kd_pressure_sensor_t,kd_pressure_sensor,'kd_pressure_sensor_t != kd_pressure_sensor. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nm_pressure_sensor_info_t,nm_pressure_sensor_info,'nm_pressure_sensor_info_t != nm_pressure_sensor_info. id_metering_device = '+id_metering_device+'')
                function_reconciliation(kd_consumed_volume_t,kd_consumed_volume,'kd_consumed_volume_t != kd_consumed_volume. id_metering_device = '+id_metering_device+'')
                function_reconciliation(id_municipal_resource_type_t,id_municipal_resource_type,'id_municipal_resource_type_t != id_municipal_resource_type. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_connection_type_t,nn_connection_type,'nn_connection_type_t != nn_connection_type. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_tariff_t,nn_tariff,'nn_tariff_t != nn_tariff. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_value_1_t,nn_value_1,'nn_value_1_t != nn_value_1. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_value_arhive_1_t,nn_value_arhive_1,'nn_value_arhive_1_t != nn_value_arhive_1. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_value_2_t,nn_value_2,'nn_value_2_t != nn_value_2. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_value_arhive_2_t,nn_value_arhive_2,'nn_value_arhive_2_t != nn_value_arhive_2. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_value_3_t,nn_value_3,'nn_value_3_t != nn_value_3. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_value_arhive_3_t,nn_value_arhive_3,'nn_value_arhive_3_t != nn_value_arhive_3. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_transformation_ratio_t,nn_transformation_ratio,'nn_transformation_ratio_t != nn_transformation_ratio. id_metering_device = '+id_metering_device+'')
                function_reconciliation(nn_archiving_type_t,nn_archiving_type,'nn_archiving_type_t != nn_archiving_type. id_metering_device = '+id_metering_device+'')
                function_reconciliation(id_reason_archiving_t,id_reason_archiving,'id_reason_archiving_t != id_reason_archiving. id_metering_device = '+id_metering_device+'')
                function_reconciliation(kd_planned_verification_t,kd_planned_verification,'kd_planned_verification_t != kd_planned_verification. id_metering_device = '+id_metering_device+'')
                function_reconciliation(id_metering_device_replace_t,id_metering_device_replace,'id_metering_device_replace_t != id_metering_device_replace. id_metering_device = '+id_metering_device+'')
                function_reconciliation(id_unit_t,id_unit,'id_unit_t != id_unit. id_metering_device = '+id_metering_device+'')

                #Проверка наличия связи абонентов со счетчиком
                kol_abonent = (len(parsed_data['metering_device'][i]['accounts']))-1           
                if kol_abonent >= 0:
                    i2=-1
                    # Работаем с i абонентом
                    while i2 < kol_abonent:
                        i2=i2+1
                        id_account = pformat(parsed_data['metering_device'][i]['accounts'][i2]['id_account'])
                        table = 'G2_STG_METERING_DEVICE_ACCOUNT'
                        field_2 = 'ID_METERING_DEVICE'
                        field2_2 = 'ID_ACCOUNT'
                        metering_device_account_count = f_count_2field(table,field_2,value,field2_2,id_account)
                        if metering_device_account_count == 0:
                            wright_txt('Не создалась связь абонента со счетчиком. ID_METERING_DEVIC: '+value+' ID_ACCOUNT: '+id_account+'')
def setMeteringDeviceValues_reconciliation(parsed_data):  #Показания приборов учета 
    Unicodeerror_h = 0
    kol_Charge = (len(parsed_data['metering_device_values']))-1 #Считаем сколько объектов в блоке metering_device_values
    i=-1
	# Работаем с i показаниями
    while i < kol_Charge:
        i=i+1
        error = ''
        table = 'G2_STG_METERING_DEVICE_VALUE' #Название таблицы хранения показаний в бд 
        field = 'ID_METERING_DEVICE_VALUE' #Название поля (иникального индификатора) в базе для поиска показаний
        nm_org_uuid = str(parsed_data['info']['nm_org_uuid']) #Получаем nm_org_uuid организации из json
        id_org = str(f_org(nm_org_uuid)) #Получаем id организации из бд
        value = pformat(parsed_data['metering_device_values'][i]['id_metering_device_values']) #Получаем id_metering_device_values из json     
        count = f_count(table,field,value) #Отправляем id_fias_guid в функцию для подсчета колличества показаний в таблице
        if count == 0: #Если показаний в базе 0
            wright_txt('Значения счетчика id_metering_device = '+value+' не найдены')
        elif count > 1: #Если показаний в базе больше 1
            wright_txt('Найдено значений счетчика больше 1 id_metering_device_value = '+value+'')
        else: #Если в базе 1 показание
            g2_stg_metering_device_value_table = rbd_conn.execute(""+generation_sql_select(table,field,value)+"")
            try: #Проверка на ошибку в кодеровке данных
                g2_stg_metering_device_value_mas = g2_stg_metering_device_value_table.fetchall()
            except UnicodeDecodeError:
                wright_txt('ошибка в кодировке данных в g2_stg_payment_table')
                Unicodeerror_h = 1
            if Unicodeerror_h == 1:
                return()
            
            if g2_stg_metering_device_value_mas[0]['nm_error_code'] != None:
                wright_txt('показания счетчика id_metering_device_values', value, 'загрузились с ошибкой. nm_error_code =', str(g2_stg_metering_device_value_mas[0]['nm_error_code']))
            else:

                #Расскладываем данные из json по переменным
                nm_exch_key = (parsed_data['metering_device_values'][i]['nm_exch_key'])
                dt_actual = parsed_date_time(str(parsed_data['metering_device_values'][i]['dt_actual']))
                id_metering_device = (parsed_data['metering_device_values'][i]['id_metering_device'])
                id_metering_device_value = (parsed_data['metering_device_values'][i]['id_metering_device_values'])
                nn_type_indication = (parsed_data['metering_device_values'][i]['nn_type_indication'])
                dt_indication = parsed_date_time(str(parsed_data['metering_device_values'][i]['dt_indication']))
                nn_value_1 = (parsed_data['metering_device_values'][i]['nn_value_1'])
                nn_value_2 = (parsed_data['metering_device_values'][i]['nn_value_2'])
                nn_value_3 = (parsed_data['metering_device_values'][i]['nn_value_3'])
                dt_start_verification = parsed_date_time(str(parsed_data['metering_device_values'][i]['dt_start_verification']))
                dt_end_verification = parsed_date_time(str(parsed_data['metering_device_values'][i]['dt_end_verification']))
                dt_seal = parsed_date_time(str(parsed_data['metering_device_values'][i]['dt_seal']))
                nn_start_value_verification_1 = (parsed_data['metering_device_values'][i]['nn_start_value_verification_1'])
                nn_start_value_verification_2 = (parsed_data['metering_device_values'][i]['nn_start_value_verification_2'])
                nn_start_value_verification_3 = (parsed_data['metering_device_values'][i]['nn_start_value_verification_3'])
                kd_planned_verification = (parsed_data['metering_device_values'][i]['kd_planned_verification'])
                id_reason_fail = (parsed_data['metering_device_values'][i]['id_failure_reason'])
                
                #Расскладываем данные из бд по переменным            
                nm_exch_key_t = (g2_stg_metering_device_value_mas[0]['nm_exch_key'])
                dt_actual_t = parsed_date_time(str(g2_stg_metering_device_value_mas[0]['dt_actual']))
                nm_org_uuid_t = (g2_stg_metering_device_value_mas[0]['nm_org_uuid'])
                id_metering_device_value_t = (g2_stg_metering_device_value_mas[0]['id_metering_device_value'])
                id_metering_device_t = (g2_stg_metering_device_value_mas[0]['id_metering_device'])
                nn_type_indication_t = (g2_stg_metering_device_value_mas[0]['nn_type_indication'])
                dt_indication_t = parsed_date_time(str(g2_stg_metering_device_value_mas[0]['dt_indication']))
                nn_value_1_t = (g2_stg_metering_device_value_mas[0]['nn_value_1'])
                nn_value_2_t = (g2_stg_metering_device_value_mas[0]['nn_value_2'])
                nn_value_3_t = (g2_stg_metering_device_value_mas[0]['nn_value_3'])
                dt_start_verification_t = parsed_date_time(str(g2_stg_metering_device_value_mas[0]['dt_start_verification']))
                dt_end_verification_t = parsed_date_time(str(g2_stg_metering_device_value_mas[0]['dt_end_verification']))
                dt_seal_t = parsed_date_time(str(g2_stg_metering_device_value_mas[0]['dt_seal']))
                nn_start_value_verification_1_t = (g2_stg_metering_device_value_mas[0]['nn_start_value_verification_1'])
                nn_start_value_verification_2_t = (g2_stg_metering_device_value_mas[0]['nn_start_value_verification_2'])
                nn_start_value_verification_3_t = (g2_stg_metering_device_value_mas[0]['nn_start_value_verification_3'])
                kd_planned_verification_t = (g2_stg_metering_device_value_mas[0]['kd_planned_verification'])
                id_reason_fail_t = (g2_stg_metering_device_value_mas[0]['id_reason_fail'])
                nm_transport_uuid_t = (g2_stg_metering_device_value_mas[0]['nm_transport_uuid'])
                nm_error_code_t = (g2_stg_metering_device_value_mas[0]['nm_error_code'])
                nm_error_description_t = (g2_stg_metering_device_value_mas[0]['nm_error_description'])

    
                #Отправляем данные в функцию сверки
                function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. id_metering_device_values = '+value+'')
                function_reconciliation(dt_actual_t,dt_actual,'dt_actual_t != dt_actual. id_metering_device_values = '+value+'')
                function_reconciliation(id_metering_device_t,id_metering_device,'id_metering_device_t != id_metering_device. id_metering_device_values = '+value+'')
                function_reconciliation(id_metering_device_value_t,id_metering_device_value,'id_metering_device_value_t != id_metering_device_value. id_metering_device_values = '+value+'')
                function_reconciliation(nn_type_indication_t,nn_type_indication,'nn_type_indication_t != nn_type_indication. id_metering_device_values = '+value+'')
                function_reconciliation(dt_indication_t,dt_indication,'dt_indication_t != dt_indication. id_metering_device_values = '+value+'')
                function_reconciliation(nn_value_1_t,nn_value_1,'nn_value_1_t != nn_value_1. id_metering_device_values = '+value+'')
                function_reconciliation(nn_value_2_t,nn_value_2,'nn_value_2_t != nn_value_2. id_metering_device_values = '+value+'')
                function_reconciliation(nn_value_3_t,nn_value_3,'nn_value_3_t != nn_value_3. id_metering_device_values = '+value+'')
                function_reconciliation(dt_start_verification_t,dt_start_verification,'dt_start_verification_t != dt_start_verification. id_metering_device_values = '+value+'')
                function_reconciliation(dt_end_verification_t,dt_end_verification,'dt_end_verification_t != dt_end_verification. id_metering_device_values = '+value+'')
                function_reconciliation(dt_seal_t,dt_seal,'dt_seal_t != dt_seal. id_metering_device_values = '+value+'')
                function_reconciliation(nn_start_value_verification_1_t,nn_start_value_verification_1,'nn_start_value_verification_1_t != nn_start_value_verification_1. id_metering_device_values = '+value+'')
                function_reconciliation(nn_start_value_verification_2_t,nn_start_value_verification_2,'nn_start_value_verification_2_t != nn_start_value_verification_2. id_metering_device_values = '+value+'')
                function_reconciliation(nn_start_value_verification_3_t,nn_start_value_verification_3,'nn_start_value_verification_3_t != nn_start_value_verification_3. id_metering_device_values = '+value+'')
                function_reconciliation(kd_planned_verification_t,kd_planned_verification,'kd_planned_verification_t != kd_planned_verification. id_metering_device_values = '+value+'')
                function_reconciliation(id_reason_fail_t,id_reason_fail,'id_reason_fail_t != id_reason_fail. id_metering_device_values = '+value+'')
def setContract_reconciliation(parsed_data):  #Договоры 
    Unicodeerror_h = 0
    kol_Contract = (len(parsed_data['contracts']))-1 #Считаем сколько объектов в блоке contracts
    i=-1
	# Работаем с i контрактом
    while i < kol_Contract:
        i=i+1
        error = ''
        table = 'G2_STG_CONTRACT' #Название таблицы хранения домов в бд 
        field = 'ID_CONTRACT' #Название поля (иникального индификатора) в базе для поиска дома
        value = pformat(parsed_data['contracts'][i]['id_contract'])     
        count = f_count(table,field,value) #Отправляем id_fias_guid в функцию для подсчета колличества контрактов в таблице
        if count == 0: #Если контрактов в базе 0
            wright_txt('Договор id_contract = '+value+' не найдены')
        elif count > 1: #Если контрактов в базе больше 1
            wright_txt('Найдено больше 1 договора id_contract = '+value+'')
        else: #Если в базе 1 контракт
            g2_stg_contract_table = rbd_conn.execute(""+generation_sql_select(table,field,value)+"")
            try: #Проверка на ошибку в кодеровке данных
                g2_stg_contract_mas = g2_stg_contract_table.fetchall()
            except UnicodeDecodeError:
                wright_txt('ошибка в кодировке данных в g2_stg_payment_table')
                Unicodeerror_h = 1
            if Unicodeerror_h == 1:
                return()

            if g2_stg_contract_mas[0]['nm_error_code'] != None:
                wright_txt('договор id_contract', value, 'загрузился с ошибкой. nm_error_code =', str(g2_stg_contract_mas[0]['nm_error_code']))
            else:
                #Расскладываем данные из json по переменным
                nm_exch_key = (parsed_data['contracts'][i]['nm_exch_key'])
                dt_actual = parsed_date_time(str(parsed_data['contracts'][i]['dt_actual']))
                nm_org_rso_uuid = (parsed_data['contracts'][i]['nm_org_rso_uuid'])
                id_contract = (parsed_data['contracts'][i]['id_contract'])
                nm_contract = (parsed_data['contracts'][i]['nm_contract'])
                nn_open = (parsed_data['contracts'][i]['nn_open'])
                dt_signing = parsed_date_time(str(parsed_data['contracts'][i]['dt_signing']))
                dt_start = parsed_date_time(str(parsed_data['contracts'][i]['dt_start']))
                dt_end = parsed_date_time(str(parsed_data['contracts'][i]['dt_end']))
                kd_prolongation = (parsed_data['contracts'][i]['kd_prolongation'])
                nn_start_counters_indication = (parsed_data['contracts'][i]['nn_start_counters_indication'])
                nn_end_counters_indication = (parsed_data['contracts'][i]['nn_end_counters_indication'])
                kd_next_month_counters_indication = (parsed_data['contracts'][i]['kd_next_month_counters_indication'])
                kd_offer = (parsed_data['contracts'][i]['kd_offer'])
                nn_owner = (parsed_data['contracts'][i]['nn_owner'])
                nn_type_owner = (parsed_data['contracts'][i]['nn_type_owner'])
                nm_surname = (parsed_data['contracts'][i]['nm_surname'])
                nm_name = (parsed_data['contracts'][i]['nm_name'])
                nm_middle_name = (parsed_data['contracts'][i]['nm_middle_name'])
                nm_sex = (parsed_data['contracts'][i]['nm_sex'])
                dt_date_birth = parsed_date_time(str(parsed_data['contracts'][i]['dt_date_birth']))
                id_identity_document = (parsed_data['contracts'][i]['id_identity_document'])
                nm_serial_identity_document = (parsed_data['contracts'][i]['nm_serial_identity_document'])
                nm_number_identity_document = (parsed_data['contracts'][i]['nm_number_identity_document'])
                dt_identity_document = parsed_date_time(str(parsed_data['contracts'][i]['dt_identity_document']))
                nm_snils = (parsed_data['contracts'][i]['nm_snils'])
                nn_state_reg_number = (parsed_data['contracts'][i]['nn_state_reg_number'])
                kd_charge_side = (parsed_data['contracts'][i]['kd_charge_side'])
                kd_counter_side = (parsed_data['contracts'][i]['kd_counter_side'])
                nn_billing_date = (parsed_data['contracts'][i]['nn_billing_date'])
                kd_billing_month = (parsed_data['contracts'][i]['kd_billing_month'])
                nn_payment_date = (parsed_data['contracts'][i]['nn_payment_date'])
                kd_payment_month = (parsed_data['contracts'][i]['kd_payment_month'])
                kd_volume_depends = (parsed_data['contracts'][i]['kd_volume_depends'])
                dt_terminate = parsed_date_time(str(parsed_data['contracts'][i]['dt_terminate']))
                id_terminate =  (parsed_data['contracts'][i]['id_termination_reason'])
                dt_rollover_end = parsed_date_time(str(parsed_data['contracts'][i]['dt_rollover_end']))



                #Расскладываем данные из бд по переменным
                nm_exch_key_t = (g2_stg_contract_mas[0]['nm_exch_key'])
                dt_actual_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_actual']))
                nm_org_rso_uuid_t = (g2_stg_contract_mas[0]['nm_org_uuid'])
                id_contract_t = (g2_stg_contract_mas[0]['id_contract'])
                nm_contract_t = (g2_stg_contract_mas[0]['nm_contract'])
                nn_open_t = (g2_stg_contract_mas[0]['nn_open'])
                dt_signing_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_signing']))
                dt_start_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_start']))
                dt_end_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_end']))
                kd_prolongation_t = (g2_stg_contract_mas[0]['kd_prolongation'])
                nn_start_counters_indication_t = (g2_stg_contract_mas[0]['nn_start_counters_indication'])
                nn_end_counters_indication_t = (g2_stg_contract_mas[0]['nn_end_counters_indication'])
                kd_next_month_counters_indication_t = (g2_stg_contract_mas[0]['kd_next_month_counters_indication'])
                kd_offer_t = (g2_stg_contract_mas[0]['kd_offer'])
                nn_owner_t = (g2_stg_contract_mas[0]['nn_owner'])
                nn_type_owner_t = (g2_stg_contract_mas[0]['nn_type_owner'])
                nm_surname_t = (g2_stg_contract_mas[0]['nm_surname'])
                nm_name_t = (g2_stg_contract_mas[0]['nm_name'])
                nm_middle_name_t = (g2_stg_contract_mas[0]['nm_middle_name'])
                nm_sex_t = (g2_stg_contract_mas[0]['nm_sex'])
                dt_date_birth_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_date_birth']))
                id_identity_document_t = (g2_stg_contract_mas[0]['id_identity_document'])
                nm_serial_identity_document_t = (g2_stg_contract_mas[0]['nm_serial_identity_document'])
                nm_number_identity_document_t = (g2_stg_contract_mas[0]['nm_number_identity_document'])
                dt_identity_document_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_identity_document']))
                nm_snils_t = (g2_stg_contract_mas[0]['nm_snils'])
                nn_state_reg_number_t = (g2_stg_contract_mas[0]['nn_state_reg_number'])
                kd_charge_side_t = (g2_stg_contract_mas[0]['kd_charge_side'])
                kd_counter_side_t = (g2_stg_contract_mas[0]['kd_counter_side'])
                nn_billing_date_t = (g2_stg_contract_mas[0]['nn_billing_date'])
                kd_billing_month_t = (g2_stg_contract_mas[0]['kd_billing_month'])
                nn_payment_date_t = (g2_stg_contract_mas[0]['nn_payment_date'])
                kd_payment_month_t = (g2_stg_contract_mas[0]['kd_payment_month'])
                kd_volume_depends_t = (g2_stg_contract_mas[0]['kd_volume_depends'])
                dt_terminate_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_terminate']))
                id_terminate_t = (g2_stg_contract_mas[0]['id_terminate'])
                dt_rollover_end_t = parsed_date_time(str(g2_stg_contract_mas[0]['dt_rollover_end']))
                contract_service_t = (g2_stg_contract_mas[0]['contract_service'])
                nm_transport_uuid_t = (g2_stg_contract_mas[0]['nm_transport_uuid'])
                nm_error_code_t = (g2_stg_contract_mas[0]['nm_error_code'])
                nm_error_description_t = (g2_stg_contract_mas[0]['nm_error_description'])
                id_fias_guid_t = (g2_stg_contract_mas[0]['id_fias_guid'])
                id_house_object_t = (g2_stg_contract_mas[0]['id_house_object'])

    
                #Отправляем данные в функцию сверки
                function_reconciliation(nm_exch_key_t,nm_exch_key,'nm_exch_key_t != nm_exch_key. id_contract = '+value+'')
                function_reconciliation(dt_actual_t,dt_actual,'dt_actual_t != dt_actual. id_contract = '+value+'')
                function_reconciliation(nm_org_rso_uuid_t,nm_org_rso_uuid,'nm_org_rso_uuid_t != nm_org_rso_uuid. id_contract = '+value+'')
                function_reconciliation(id_contract_t,id_contract,'id_contract_t != id_contract. id_contract = '+value+'')
                function_reconciliation(nm_contract_t,nm_contract,'nm_contract_t != nm_contract. id_contract = '+value+'')
                function_reconciliation(nn_open_t,nn_open,'nn_open_t != nn_open. id_contract = '+value+'')
                function_reconciliation(dt_signing_t,dt_signing,'dt_signing_t != dt_signing. id_contract = '+value+'')
                function_reconciliation(dt_start_t,dt_start,'dt_start_t != dt_start. id_contract = '+value+'')
                function_reconciliation(dt_end_t,dt_end,'dt_end_t != dt_end. id_contract = '+value+'')
                function_reconciliation(kd_prolongation_t,kd_prolongation,'kd_prolongation_t != kd_prolongation. id_contract = '+value+'')
                function_reconciliation(nn_start_counters_indication_t,nn_start_counters_indication,'nn_start_counters_indication_t != nn_start_counters_indication. id_contract = '+value+'')
                function_reconciliation(nn_end_counters_indication_t,nn_end_counters_indication,'nn_end_counters_indication_t != nn_end_counters_indication. id_contract = '+value+'')
                function_reconciliation(kd_next_month_counters_indication_t,kd_next_month_counters_indication,'kd_next_month_counters_indication_t != kd_next_month_counters_indication. id_contract = '+value+'')
                function_reconciliation(kd_offer_t,kd_offer,'kd_offer_t != kd_offer. id_contract = '+value+'')
                function_reconciliation(nn_owner_t,nn_owner,'nn_owner_t != nn_owner. id_contract = '+value+'')
                function_reconciliation(nn_type_owner_t,nn_type_owner,'nn_type_owner_t != nn_type_owner. id_contract = '+value+'')
                function_reconciliation(nm_surname_t,nm_surname,'nm_surname_t != nm_surname. id_contract = '+value+'')
                function_reconciliation(nm_name_t,nm_name,'nm_name_t != nm_name. id_contract = '+value+'')
                function_reconciliation(nm_middle_name_t,nm_middle_name,'nm_middle_name_t != nm_middle_name. id_contract = '+value+'')
                function_reconciliation(nm_sex_t,nm_sex,'nm_sex_t != nm_sex. id_contract = '+value+'')
                function_reconciliation(dt_date_birth_t,dt_date_birth,'dt_date_birth_t != dt_date_birth. id_contract = '+value+'')
                function_reconciliation(id_identity_document_t,id_identity_document,'id_identity_document_t != id_identity_document. id_contract = '+value+'')
                function_reconciliation(nm_serial_identity_document_t,nm_serial_identity_document,'nm_serial_identity_document_t != nm_serial_identity_document. id_contract = '+value+'')
                function_reconciliation(nm_number_identity_document_t,nm_number_identity_document,'nm_number_identity_document_t != nm_number_identity_document. id_contract = '+value+'')
                function_reconciliation(dt_identity_document_t,dt_identity_document,'dt_identity_document_t != dt_identity_document. id_contract = '+value+'')
                function_reconciliation(nm_snils_t,nm_snils,'nm_snils_t != nm_snils. id_contract = '+value+'')
                function_reconciliation(nn_state_reg_number_t,nn_state_reg_number,'nn_state_reg_number_t != nn_state_reg_number. id_contract = '+value+'')
                function_reconciliation(kd_charge_side_t,kd_charge_side,'kd_charge_side_t != kd_charge_side. id_contract = '+value+'')
                function_reconciliation(kd_counter_side_t,kd_counter_side,'kd_counter_side_t != kd_counter_side. id_contract = '+value+'')
                function_reconciliation(nn_billing_date_t,nn_billing_date,'nn_billing_date_t != nn_billing_date. id_contract = '+value+'')
                function_reconciliation(kd_billing_month_t,kd_billing_month,'kd_billing_month_t != kd_billing_month. id_contract = '+value+'')
                function_reconciliation(nn_payment_date_t,nn_payment_date,'nn_payment_date_t != nn_payment_date. id_contract = '+value+'')
                function_reconciliation(kd_payment_month_t,kd_payment_month,'kd_payment_month_t != kd_payment_month. id_contract = '+value+'')
                function_reconciliation(kd_volume_depends_t,kd_volume_depends,'kd_volume_depends_t != kd_volume_depends. id_contract = '+value+'')
                function_reconciliation(dt_terminate_t,dt_terminate,'dt_terminate_t != dt_terminate. id_contract = '+value+'')
                function_reconciliation(id_terminate_t,id_terminate,'id_terminate_t != id_terminate. id_contract = '+value+'')
                function_reconciliation(dt_rollover_end_t,dt_rollover_end,'dt_rollover_end_t != dt_rollover_end. id_contract = '+value+'')

                kol_contract_subject = (len(parsed_data['contracts'][i]['contract_subject']))-1 #Считаем сколько объектов в блоке contracts
                i2=-1
                # Работаем с i контрактом
                while i2 < kol_contract_subject:           
                    i2=i2+1
                    #Расскладываем данные из json contract_subject по переменным
                    id_service_type = (parsed_data['contracts'][i]['contract_subject'][i2]['id_service_type'])
                    id_municipal_resource = (parsed_data['contracts'][i]['contract_subject'][i2]['id_municipal_resource'])

                    dt_start_resource = parsed_date_time(str(parsed_data['contracts'][i]['contract_subject'][i2]['dt_start_resource']))
                    dt_end_resource = parsed_date_time(str(parsed_data['contracts'][i]['contract_subject'][i2]['dt_end_resource']))
                    nn_heating_system_form = (parsed_data['contracts'][i]['contract_subject'][i2]['nn_heating_system_form'])
                    nn_heating_system_type = (parsed_data['contracts'][i]['contract_subject'][i2]['nn_heating_system_type'])

                    table2 = 'G2_STG_CONTRACT_SUBJECT' #Название таблицы хранения домов в бд 
                    field2 = 'ID_CONTRACT' #Название поля (иникального индификатора) в базе для поиска дома
                    field3 = 'ID_MUNICIPAL_RESOURCE' #Название поля (иникального индификатора) в базе для поиска дома
                    value2 = pformat(parsed_data['contracts'][i]['id_contract'])     
                    value3 = str(parsed_data['contracts'][i]['contract_subject'][i2]['id_municipal_resource'])
                    count_2 = f_count_2field(table2,field2,value2,field3,value3) #Отправляем id_fias_guid в функцию для подсчета колличества контрактов в таблице
                    if count_2 == 0: #Если контрактов в базе 0
                        wright_txt('Объекта  договора id_contract = '+value+' не найден')
                        return()
                    elif count_2 > 1: #Если контрактов в базе больше 1
                        wright_txt('Найдено больше 1 объекта договора id_contract = '+value+'')
                        return()
                    else: #Если в базе 1 контракт
                        g2_stg_contract_subject_table = rbd_conn.execute(""+generation_sql_select_2field(table2,field2,value2,field3,value3)+"")
                        try: #Проверка на ошибку в кодеровке данных
                            g2_stg_contract_subject_mas = g2_stg_contract_subject_table.fetchall()
                        except UnicodeDecodeError:
                            wright_txt('ошибка в кодировке данных в g2_stg_payment_table')
                            Unicodeerror_h = 1
                        if Unicodeerror_h == 1:
                            return()

                    id_service_type_t = (g2_stg_contract_subject_mas[0]['id_service_type'])
                    dt_start_resource_t = parsed_date_time(str(g2_stg_contract_subject_mas[0]['dt_start_resource']))
                    dt_end_resource_t = parsed_date_time(str(g2_stg_contract_subject_mas[0]['dt_end_resource']))
                    nn_heating_system_form_t = (g2_stg_contract_subject_mas[0]['nn_heating_system_form'])
                    nn_heating_system_type_t = (g2_stg_contract_subject_mas[0]['nn_heating_system_type'])

                    function_reconciliation(id_service_type_t,id_service_type,'id_service_type_t != id_service_type. id_contract = '+value2+'')
                    function_reconciliation(dt_start_resource_t,dt_start_resource,'dt_start_resource_t != dt_start_resource. id_contract = '+value2+'')
                    function_reconciliation(dt_end_resource_t,dt_end_resource,'dt_terminate_t != dt_terminate. id_contract = '+value2+'')
                    function_reconciliation(nn_heating_system_form_t,nn_heating_system_form,'nn_heating_system_form_t != nn_heating_system_form. id_contract = '+value2+'')
                    function_reconciliation(nn_heating_system_type_t,nn_heating_system_type,'nn_heating_system_type_t != nn_heating_system_type. id_contract = '+value2+'')
                    

def setAccountSuccessfully(): 
    service = 'setAccount'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:  

        name_test = 'Succ_LS0001'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        parsed_data,answer = f_load_json(Json_setAccount,service)
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0002'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nm_account'] = '465456456'
        parsed_data,answer = f_load_json(Json_setAccount,service)
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)

        name_test = 'Succ_LS0002'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nm_account'] = '465456456'
        parsed_data,answer = f_load_json(Json_setAccount,service)
        response_answer(answer,error,Json_setAccount,name_test)

        name_test = 'Succ_LS0003_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['kd_open'] = 1
        parsed_data,answer = f_load_json(Json_setAccount,service)
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0005'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nn_living_people_number'] = 3
        parsed_data,answer = f_load_json(Json_setAccount,service)        
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0006'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['kd_open'] = 0
        Json_setAccount['account'][0]['dt_close'] = '2020-06-02T10:31:06'
        Json_setAccount['account'][0]['id_closing_reason'] = 14
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)

        name_test = 'Succ_LS0008_4'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 4
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0009'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['contracts'][0]['id_contract'] = '978455'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)


        #----------------------------------------------------------------------
        name_test = 'Succ_LS0016'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 1
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = 'rt'
        Json_setAccount['account'][0]['nm_name'] = 'ва'
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = '6345345'
        Json_setAccount['account'][0]['nm_snils'] = '342342'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)

        #----------------------------------------------------------------------------

        name_test = 'Succ_LS0016_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 3
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = 'try'
        Json_setAccount['account'][0]['nm_name'] = 'ва'
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = '6345345'
        Json_setAccount['account'][0]['nm_snils'] = '342342'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)

        name_test = 'Succ_LS0016_3'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 2
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nn_state_reg_number'] = 45
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)

        name_test = 'Succ_LS0017'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nn_total_area'] = 68.3
        Json_setAccount['account'][0]['nn_residential_area'] = 66.3
        Json_setAccount['account'][0]['nn_heated_area'] = 68.3
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0017_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nn_total_area'] = 68.3
        Json_setAccount['account'][0]['nn_residential_area'] = 68.3
        Json_setAccount['account'][0]['nn_heated_area'] = 66.3
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0018'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['nm_exch_key'] = '895'
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0019'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['dt_actual'] = '2020-06-02T10:31:06'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0020'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = '985444'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
        
        name_test = 'Succ_LS0021'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['kd_hold'] = 0
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)

        name_test = 'Succ_LS0021_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        id_fias_guid,id_house_object = created_addr_house(name_test)
        Json_setAccount = generation_Account(id_fias_guid, id_house_object)
        Json_setAccount['account'][0]['kd_hold'] = 1
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        setAccount_reconciliation(parsed_data)
def setAddrObjDataSuccessfully(): #тест на апдейт данных по абоненту
    service = 'setAddrObjData'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:    

        name_test = 'Succ_ADR0001'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        Json_setAddrObjData['address_object'][0]['dt_actual'] = '2020-10-02T12:01:12'
        Json_setAddrObjData['address_object'][0]['nm_exch_key'] = '546'
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0003_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 2
        Json_setAddrObjData['address_object'][0]['nm_oktmo'] = '12345678911'
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0003_3'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setAddrObjData['address_object'][0]['nm_oktmo'] = '12345678'
        Json_setAddrObjData['address_object'][0]['nm_postcode'] = '123456'
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0003_4'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0006'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['kd_houses_same_address'] = 1
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3       
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        # name_test = 'Succ_ADR0010'
        # error = 'HO0003'
        # Json_setAddrObjData = generation_AddrObjData()
        # Json_setAddrObjData['address_object'][0]['house_object'][0]['nn_type_object'] = 1
        # Json_setAddrObjData['address_object'][0]['house_object'][0]['nm_entrance'] = ''
        # parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        # response_answer(answer,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR0016_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0017'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0017_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0017_3'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0017_4'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0018_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0018_4'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0020'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 2
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0022'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0022_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0023'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)

        name_test = 'Succ_ADR0023_2'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        setAddrObjData_reconciliation(parsed_data)
def setHouseObjDataSuccessfully(): #тест на апдейт данных по абоненту
    service = 'setHouseObjData'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:  

        name_test = 'Succ_ADR00'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR01'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 6
        Json_setHouseObjData['house_object'][0]['nm_premises'] = '54'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '5'
        Json_setAddrObjData['address_object'][0]['dt_actual'] = '2020-10-02T12:01:12'
        Json_setAddrObjData['address_object'][0]['nm_exch_key'] = '546'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR02'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 2
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 7
        Json_setHouseObjData['house_object'][0]['nm_room'] = '67'
        Json_setAddrObjData['address_object'][0]['nm_oktmo'] = '12345678911'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR03'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 2
        Json_setHouseObjData['house_object'][0]['nm_block'] = '67'
        Json_setAddrObjData['address_object'][0]['nm_oktmo'] = '12345678'
        Json_setAddrObjData['address_object'][0]['nm_postcode'] = '123456'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR04'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        Json_setHouseObjData['house_object'][0]['id_fias_guid_parent'] = 'd00a38ae-8650-49ff-993f-09f01cd4694c'
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 6
        Json_setHouseObjData['house_object'][0]['nm_premises'] = '89'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '5'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR05'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['kd_houses_same_address'] = 1 
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nm_block'] = '34'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR06'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 1
        Json_setHouseObjData['house_object'][0]['nm_entrance'] = '78'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR07'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 3
        Json_setHouseObjData['house_object'][0]['nm_block'] = '34'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR08'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 8
        Json_setHouseObjData['house_object'][0]['nm_block'] = '34'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '34'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR09'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 4
        Json_setHouseObjData['house_object'][0]['nm_premises'] = '342'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR10'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 5
        Json_setHouseObjData['house_object'][0]['nm_premises'] = '234'
        Json_setHouseObjData['house_object'][0]['id_reasons_cancell'] = 0
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR11'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 8
        Json_setHouseObjData['house_object'][0]['nm_block'] = '4'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '523'
        Json_setHouseObjData['house_object'][0]['id_reasons_cancell'] = 6
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR12'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 1
        Json_setHouseObjData['house_object'][0]['nm_entrance'] = '34'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR13'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 4
        Json_setHouseObjData['house_object'][0]['nm_entrance'] = '78'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR14'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 5
        Json_setHouseObjData['house_object'][0]['nm_entrance'] = '78'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR15'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 4
        Json_setHouseObjData['house_object'][0]['nm_entrance'] = '89'
        Json_setHouseObjData['house_object'][0]['id_fias_guid_parent'] = 'd00a77ae-8650-49ff-993f-09f01cd4694c'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR16'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 5
        Json_setHouseObjData['house_object'][0]['nm_entrance'] = '89'
        Json_setHouseObjData['house_object'][0]['id_fias_guid_parent'] = 'd00a77ae-8650-49ff-993f-09f01cd4694c'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR17'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 1
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 6
        Json_setHouseObjData['house_object'][0]['nm_premises'] = '5'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '54'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR18'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 4
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 6
        Json_setHouseObjData['house_object'][0]['nm_premises'] = '5'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '67'
        Json_setHouseObjData['house_object'][0]['id_fias_guid_parent'] = 'd00a77ae-8650-49ff-993f-09f01cd4694c'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR19'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 2
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 7
        Json_setHouseObjData['house_object'][0]['nm_room'] = '67'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR20'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 2
        Json_setHouseObjData['house_object'][0]['nm_block'] = '45'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR21'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 3
        Json_setHouseObjData['house_object'][0]['nm_block'] = '65'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR22'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 8
        Json_setHouseObjData['house_object'][0]['nm_block'] = '76'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '4'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)

        name_test = 'Succ_ADR23'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 3
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 8
        Json_setHouseObjData['house_object'][0]['nm_block'] = '4'
        Json_setHouseObjData['house_object'][0]['nm_room'] = '76'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_1_json = answer_1.json()
        if (answer_1_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            setAddrObjHouse_reconciliation(parsed_data)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_1,error,Json_setAddrObjData,name_test)
def setChargeDocumentSuccessfully(): #тест на апдейт данных по абоненту
    service = 'setChargeDocument'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:    
      
        name_test = 'Succ_PD00'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        #Проверка
        response_answer(answer,error,Json_setChargeDocument,name_test)
        setChargeDocument_reconciliation(parsed_data)

        name_test = 'Succ_PD01'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['nm_exch_key'] = '523'
        Json_setChargeDocument['charge_document'][0]['dt_actual'] = '2019-02-17T17:04:00'
        Json_setChargeDocument['charge_document'][0]['id_charge_document'] = (Generation_guid()).replace('-','')
        Json_setChargeDocument['charge_document'][0]['id_account'] = '0102000012333'
        Json_setChargeDocument['charge_document'][0]['nm_account'] = '1236987'
        Json_setChargeDocument['charge_document'][0]['dt_charge'] = '2019-02-01T00:00:00'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['nm_org_pu_uuid'] = 'ed5e0da8-65f1-4cbf-83a3-110fae2f83ec'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 2
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '1'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_tariff'] = 5.6
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_total_accrued'] = 89.20
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        setChargeDocument_reconciliation(parsed_data)

        name_test = 'Succ_PD02'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['nm_exch_key'] = '523'
        Json_setChargeDocument['charge_document'][0]['dt_actual'] = '2019-02-17T17:04:00'
        Json_setChargeDocument['charge_document'][0]['id_charge_document'] = (Generation_guid()).replace('-','')
        Json_setChargeDocument['charge_document'][0]['id_account'] = '0102000012333'
        Json_setChargeDocument['charge_document'][0]['nm_account'] = '1236987'
        Json_setChargeDocument['charge_document'][0]['dt_charge'] = '2019-02-01T00:00:00'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['nm_org_pu_uuid'] = 'ed5e0da8-65f1-4cbf-83a3-110fae2f83ec'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 4
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '2'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_tariff'] = 5.6
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_total_accrued'] = 89.20
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        #Проверка
        response_answer(answer,error,Json_setChargeDocument,name_test)
        setChargeDocument_reconciliation(parsed_data)

        name_test = 'Succ_PD03'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['nm_exch_key'] = '523'
        Json_setChargeDocument['charge_document'][0]['dt_actual'] = '2019-02-17T17:04:00'
        Json_setChargeDocument['charge_document'][0]['id_charge_document'] = (Generation_guid()).replace('-','')
        Json_setChargeDocument['charge_document'][0]['id_account'] = '0102000012333'
        Json_setChargeDocument['charge_document'][0]['nm_account'] = '1236987'
        Json_setChargeDocument['charge_document'][0]['dt_charge'] = '2019-02-01T00:00:00'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['nm_org_pu_uuid'] = 'ed5e0da8-65f1-4cbf-83a3-110fae2f83ec'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 5
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '1'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_tariff'] = 5.6
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_total_accrued'] = 89.20
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        #Проверка
        response_answer(answer,error,Json_setChargeDocument,name_test)
        setChargeDocument_reconciliation(parsed_data)


        name_test = 'Succ_PD04'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['nm_exch_key'] = '523'
        Json_setChargeDocument['charge_document'][0]['dt_actual'] = '2019-02-17T17:04:00'
        Json_setChargeDocument['charge_document'][0]['id_charge_document'] = (Generation_guid()).replace('-','')
        Json_setChargeDocument['charge_document'][0]['id_account'] = '0102000012333'
        Json_setChargeDocument['charge_document'][0]['nm_account'] = '1236987'
        Json_setChargeDocument['charge_document'][0]['dt_charge'] = '2019-02-01T00:00:00'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['nm_org_pu_uuid'] = 'ed5e0da8-65f1-4cbf-83a3-110fae2f83ec'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 6
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '1'
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_tariff'] = 5.60
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_total_accrued'] = 89.20
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        #Проверка
        response_answer(answer,error,Json_setChargeDocument,name_test)
        setChargeDocument_reconciliation(parsed_data)


        # name_test = 'PD0017'
        # error = 'PD0017'
        # Json_setChargeDocument = generation_ChargeDocument()
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_total_pay'] = None
        # parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        # response_answer(answer,error,Json_setChargeDocument,name_test)

        # name_test = 'PD0018'
        # error = 'PD0018'
        # Json_setChargeDocument = generation_ChargeDocument()
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_corr'] = 1.0
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_info_corr'] = ''
        # parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        # response_answer(answer,error,Json_setChargeDocument,name_test)

        # name_test = 'PD0020'
        # error = 'PD0020'
        # Json_setChargeDocument = generation_ChargeDocument()
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_installment'] = 1.0
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_rate_installment'] = None
        # parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        # response_answer(answer,error,Json_setChargeDocument,name_test)
        
        # name_test = 'PD0020_2'
        # error = 'PD0020'
        # Json_setChargeDocument = generation_ChargeDocument()
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_installment'] = 1.0
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_rate_installment'] = 101.0
        # parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        # response_answer(answer,error,Json_setChargeDocument,name_test)

        # name_test = 'PD0021'
        # error = 'PD0021'
        # Json_setChargeDocument = generation_ChargeDocument()
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_installment'] = 1.0
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_rate_installment'] = 1.0
        # Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_pay_with_installment_rate'] = None
        # parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        # response_answer(answer,error,Json_setChargeDocument,name_test)
def setMeteringDeviceSuccessfully(): 
    service = 'setMeteringDevice'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:  
      
        id_fias_guid,id_house_object = created_addr_house('Succ_setMeteringDeviceSuccessfully')    

        name_test = 'Succ_PU00'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        setMeteringDevice_reconciliation(parsed_data)

        name_test = 'Succ_PU01'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        Json_setMeteringDevice['metering_device'][0]['id_metering_device'] = (Generation_guid()).replace('-','')
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 1
        Json_setMeteringDevice['metering_device'][0]['id_archiving_reason'] = 1
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        setMeteringDevice_reconciliation(parsed_data)

        name_test = 'Succ_PU02'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        Json_setMeteringDevice['metering_device'][0]['id_metering_device'] = '2016853e-2282-11e'
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2
        Json_setMeteringDevice['metering_device'][0]['kd_planned_verification'] = 0
        Json_setMeteringDevice['metering_device'][0]['id_metering_device_replace'] = '36363'
        Json_setMeteringDevice['metering_device'][0]['id_failure_reason'] = 3
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        response_answer(answer,error,Json_setMeteringDevice,name_test)

        name_test = 'Succ_PU03'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        Json_setMeteringDevice['metering_device'][0]['id_metering_device'] = '2016853e-2282-11e'
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2
        Json_setMeteringDevice['metering_device'][0]['kd_planned_verification'] = 1
        Json_setMeteringDevice['metering_device'][0]['id_metering_device_replace'] = '346353'
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        response_answer(answer,error,Json_setMeteringDevice,name_test)

        name_test = 'Succ_PU04'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        Json_setMeteringDevice['metering_device'][0]['id_metering_device'] = '2016853e-2282-11e'
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_type_meter'] = 2
        Json_setMeteringDevice['metering_device'][0]['kd_consumed_volume'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = 2
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        response_answer(answer,error,Json_setMeteringDevice,name_test)

        name_test = 'Succ_PU05'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        Json_setMeteringDevice['metering_device'][0]['id_metering_device'] = '2016853e-2282-11e'
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_type_meter'] = 3
        Json_setMeteringDevice['metering_device'][0]['kd_consumed_volume'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = 3
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        response_answer(answer,error,Json_setMeteringDevice,name_test)
def setMeteringDeviceValueSuccessfully(): 
    service = 'setMeteringDeviceValues'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:  

        name_test = 'Succ_PPU00'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        setMeteringDeviceValues_reconciliation(parsed_data)

        name_test = 'Succ_PPU01'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['id_metering_device_values'] = (Generation_guid()).replace('-','')
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 1
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        setMeteringDeviceValues_reconciliation(parsed_data)

        name_test = 'Succ_PPU02'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['id_metering_device_values'] = '201685'
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 2
        Json_setMeteringDV['metering_device_values'][0]['dt_start_verification'] = '2012-02-10T00:00:00'
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)

        name_test = 'Succ_PPU03'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['id_metering_device_values'] = '201685'
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 3
        Json_setMeteringDV['metering_device_values'][0]['dt_start_verification'] = '2012-02-10T00:00:00'
        Json_setMeteringDV['metering_device_values'][0]['dt_end_verification'] = '2013-02-10T00:00:00'
        Json_setMeteringDV['metering_device_values'][0]['id_failure_reason'] = 5
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
def setContractSuccessfully(): 
    service = 'setContract'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:  

        id_fias_guid,id_house_object = created_addr_house('setContractSuccessfully')    

        name_test = 'Succ_DOG00'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        setContract_reconciliation(parsed_data)
        
        name_test = 'Succ_DOG01'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['id_contract'] = (Generation_guid()).replace('-','')
        Json_setContract['contracts'][0]['nn_open'] = 1
        Json_setContract['contracts'][0]['dt_signing'] = '1999-01-01T00:00:00'
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 1
        Json_setContract['contracts'][0]['nn_type_owner'] = 1
        Json_setContract['contracts'][0]['id_identity_document'] = 1
        Json_setContract['contracts'][0]['nm_number_identity_document'] = '363434'
        Json_setContract['contracts'][0]['dt_identity_document'] = '2020-06-02T10:31:02'
        Json_setContract['contracts'][0]['nn_billing_date'] = 0
        Json_setContract['contracts'][0]['kd_billing_month'] = 0
        Json_setContract['contracts'][0]['contract_subject'][0]['id_municipal_resource'] = 1
        Json_setContract['contracts'][0]['contract_subject'][0]['id_service_type'] = "1"
        Json_setContract['contracts'][0]['dt_start'] = '2012-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_start_resource'] = '2013-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_end_resource'] = '2014-04-27T00:00:00'
        Json_setContract['contracts'][0]['dt_end'] = '2015-04-27T00:00:00'  
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        setContract_reconciliation(parsed_data)

        name_test = 'Succ_DOG02'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['id_contract'] = (Generation_guid()).replace('-','')
        Json_setContract['contracts'][0]['nn_open'] = 2
        Json_setContract['contracts'][0]['dt_signing'] = '1999-01-01T00:00:00'
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 2
        Json_setContract['contracts'][0]['nn_state_reg_number'] = 1234567890123
        Json_setContract['contracts'][0]['nn_billing_date'] = 1
        Json_setContract['contracts'][0]['kd_billing_month'] = 1
        Json_setContract['contracts'][0]['contract_subject'][0]['id_municipal_resource'] = 2
        Json_setContract['contracts'][0]['contract_subject'][0]['id_service_type'] = "2"
        Json_setContract['contracts'][0]['dt_start'] = '2012-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_start_resource'] = '2013-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_end_resource'] = '2014-04-27T00:00:00'
        Json_setContract['contracts'][0]['dt_end'] = '2015-04-27T00:00:00'
        Json_setContract['contracts'][0]['id_termination_reason'] = 8  
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        setContract_reconciliation(parsed_data)

        name_test = 'Succ_DOG03'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['id_contract'] = (Generation_guid()).replace('-','')
        Json_setContract['contracts'][0]['nn_open'] = 3
        Json_setContract['contracts'][0]['dt_signing'] = '1999-01-01T00:00:00'
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 3
        Json_setContract['contracts'][0]['nn_type_owner'] = 3
        Json_setContract['contracts'][0]['nn_state_reg_number'] = 123456789012345
        Json_setContract['contracts'][0]['nn_billing_date'] = 0
        Json_setContract['contracts'][0]['kd_billing_month'] = 0
        Json_setContract['contracts'][0]['contract_subject'][0]['id_municipal_resource'] = 3
        Json_setContract['contracts'][0]['contract_subject'][0]['id_service_type'] = "3"
        Json_setContract['contracts'][0]['dt_start'] = '2012-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_start_resource'] = '2013-04-27T00:00:00' 
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_end_resource'] = '2014-04-27T00:00:00'
        Json_setContract['contracts'][0]['dt_end'] = '2015-04-27T00:00:00'   
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        setContract_reconciliation(parsed_data)

        name_test = 'Succ_DOG04'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['id_contract'] = (Generation_guid()).replace('-','')
        Json_setContract['contracts'][0]['nn_open'] = 4
        Json_setContract['contracts'][0]['dt_signing'] = '1999-01-01T00:00:00'
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 4
        Json_setContract['contracts'][0]['nn_type_owner'] = 4
        Json_setContract['contracts'][0]['nn_state_reg_number'] = 12345678901
        Json_setContract['contracts'][0]['nn_billing_date'] = 0
        Json_setContract['contracts'][0]['kd_billing_month'] = 0
        Json_setContract['contracts'][0]['contract_subject'][0]['id_municipal_resource'] = 4
        Json_setContract['contracts'][0]['contract_subject'][0]['id_service_type'] = "4"
        Json_setContract['contracts'][0]['dt_start'] = '2012-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_start_resource'] = '2013-04-27T00:00:00'
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_end_resource'] = '2014-04-27T00:00:00'
        Json_setContract['contracts'][0]['dt_end'] = '2015-04-27T00:00:00'    
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        setContract_reconciliation(parsed_data)

        name_test = 'Succ_DOG05'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['id_contract'] = (Generation_guid()).replace('-','')
        Json_setContract['contracts'][0]['nn_open'] = 4
        Json_setContract['contracts'][0]['dt_signing'] = '1999-01-01T00:00:00'
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 5
        Json_setContract['contracts'][0]['nn_billing_date'] = 0
        Json_setContract['contracts'][0]['kd_billing_month'] = 0
        Json_setContract['contracts'][0]['contract_subject'][0]['id_municipal_resource'] = 5
        Json_setContract['contracts'][0]['contract_subject'][0]['id_service_type'] = "5"
        Json_setContract['contracts'][0]['dt_start'] = '2012-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_start_resource'] = '2013-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_end_resource'] = '2014-04-27T00:00:00'
        Json_setContract['contracts'][0]['dt_end'] = '2015-04-27T00:00:00'  
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        setContract_reconciliation(parsed_data)

        name_test = 'Succ_DOG06'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['id_contract'] = (Generation_guid()).replace('-','')
        Json_setContract['contracts'][0]['nn_open'] = 4
        Json_setContract['contracts'][0]['dt_signing'] = '2012-04-27T00:00:00'
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 5
        Json_setContract['contracts'][0]['nn_billing_date'] = 0
        Json_setContract['contracts'][0]['kd_billing_month'] = 0
        Json_setContract['contracts'][0]['contract_subject'][0]['id_municipal_resource'] = 5
        Json_setContract['contracts'][0]['contract_subject'][0]['id_service_type'] = "5"
        Json_setContract['contracts'][0]['dt_start'] = '2012-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_start_resource'] = '2012-04-27T00:00:00'  
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_end_resource'] = '2014-04-27T00:00:00'
        Json_setContract['contracts'][0]['dt_end'] = '2015-04-27T00:00:00'  
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        setContract_reconciliation(parsed_data)
def setPaymentsSuccessfully(): 
    service = 'setPayments'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:  

        name_test = 'Succ_00'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        setPayments_reconciliation(parsed_data)

        name_test = 'Succ_01'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['id_payment'] = (Generation_guid()).replace('-','')
        Json_setPayments['payments'][0]['id_account'] = '4635445'
        Json_setPayments['payments'][0]['dt_pay'] = '2020-01-01T00:00:00'
        Json_setPayments['payments'][0]['dt_period'] = '2020-01-01T00:00:00'
        Json_setPayments['payments'][0]['nn_sm_pay'] = 45.1
        Json_setPayments['payments'][0]['kd_cancel'] = 1
        Json_setPayments['payments'][0]['dt_pay_cancel'] = '2020-02-01T00:00:00'
        Json_setPayments['payments'][0]['nm_exch_key'] = '5334'
        Json_setPayments['payments'][0]['id_ipd'] = '342'
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        setPayments_reconciliation(parsed_data)

        name_test = 'Succ_02'
        error = 'CREATED'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['id_payment'] = (Generation_guid()).replace('-','')
        Json_setPayments['payments'][0]['id_account'] = '4635445'
        Json_setPayments['payments'][0]['dt_pay'] = '2020-01-01T00:00:00'
        Json_setPayments['payments'][0]['dt_period'] = '2020-01-01T00:00:00'
        Json_setPayments['payments'][0]['nn_sm_pay'] = 45.1
        Json_setPayments['payments'][0]['kd_cancel'] = 1
        Json_setPayments['payments'][0]['dt_pay_cancel'] = '2020-02-01T00:00:00'
        Json_setPayments['payments'][0]['nm_exch_key'] = '5334'
        Json_setPayments['payments'][0]['id_zhku'] = '342'
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        setPayments_reconciliation(parsed_data)

def setAccountError(): #тест на апдейт данных по абоненту
    service = 'setAccount'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:     

        id_fias_guid,id_house_object = created_addr_house('setAccountError')  

        name_test = 'LS0001 Пустой id_account'
        error = 'LS0001'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['id_account'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service)
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,1)

        name_test = 'LS0002 Пустой nm_account'
        error = 'LS0002'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nm_account'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service)
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0003 Пустой kd_open'
        error = 'LS0003'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['kd_open'] = None
        parsed_data,answer = f_load_json(Json_setAccount,service)
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0005 Пустой nn_living_people_number'
        error = 'LS0005'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_living_people_number'] = None
        parsed_data,answer = f_load_json(Json_setAccount,service)        
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0006 kd_open = 0 dt_close = пусто'
        error = 'LS0006'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['kd_open'] = 0
        Json_setAccount['account'][0]['dt_close'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0007'
        error = 'LS0007'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['kd_open'] = 0
        Json_setAccount['account'][0]['dt_close'] = '2018-10-17T12:01:13'
        Json_setAccount['account'][0]['id_closing_reason'] = 15
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0008'
        error = 'LS0008'
        wright_txt(str(name_test))
        #Получаем массивы данных для json 
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = None
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0008_2'
        error = 'LS0008'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 5
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0009'
        error = 'LS0009'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['contracts'][0]['id_contract'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 1
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = ''
        Json_setAccount['account'][0]['nm_name'] = 'ва'
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = '6345345'
        Json_setAccount['account'][0]['nm_snils'] = '342342'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016_2'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 1
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = 'ва'
        Json_setAccount['account'][0]['nm_name'] = ''
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = '6345345'
        Json_setAccount['account'][0]['nm_snils'] = '342342'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016_3'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 1
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = 'ва'
        Json_setAccount['account'][0]['nm_name'] = 'па'
        Json_setAccount['account'][0]['id_identity_document'] = None
        Json_setAccount['account'][0]['nm_number_identity_document'] = ''
        Json_setAccount['account'][0]['nm_snils'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016_4'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 3
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = ''
        Json_setAccount['account'][0]['nm_name'] = 'ва'
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = '6345345'
        Json_setAccount['account'][0]['nm_snils'] = '342342'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016_5'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 3
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = 'ва'
        Json_setAccount['account'][0]['nm_name'] = ''
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = '6345345'
        Json_setAccount['account'][0]['nm_snils'] = '342342'
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016_6'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 3
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nm_surname'] = 'ва'
        Json_setAccount['account'][0]['nm_name'] = 'па'
        Json_setAccount['account'][0]['id_identity_document'] = None
        Json_setAccount['account'][0]['nm_number_identity_document'] = ''
        Json_setAccount['account'][0]['nm_snils'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016_7'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 2
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nn_state_reg_number'] = None
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0016_8'
        error = 'LS0016'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_type_owner'] = 4
        Json_setAccount['account'][0]['nn_own_percent'] = 99
        Json_setAccount['account'][0]['nn_state_reg_number'] = None
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0017'
        error = 'LS0017'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_total_area'] = 65.3
        Json_setAccount['account'][0]['nn_residential_area'] = 66.3
        Json_setAccount['account'][0]['nn_heated_area'] = 65.3
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0017_2'
        error = 'LS0017'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nn_total_area'] = 65.3
        Json_setAccount['account'][0]['nn_residential_area'] = 65.3
        Json_setAccount['account'][0]['nn_heated_area'] = 66.3
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0018 Пустой nm_exch_key'
        error = 'LS0018'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['nm_exch_key'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service)  
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','ID_ACCOUNT',pformat(Json_setAccount['account'][0]['id_account']),'','', error,name_test,1,Json_setAccount,1)

        name_test = 'LS0019 Пустая dt_actual'
        error = 'LS0019'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['dt_actual'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,1)

        name_test = 'LS0020'
        error = 'LS0020'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['id_identity_document'] = 1
        Json_setAccount['account'][0]['nm_number_identity_document'] = ''
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)

        name_test = 'LS0021'
        error = 'LS0021'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['kd_hold'] = None
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)
        
        name_test = 'LS0021_2'
        error = 'LS0021'
        wright_txt(str(name_test))
        #Получаем массивы данных для json
        Json_setAccount = generation_Account(id_fias_guid,id_house_object)
        Json_setAccount['account'][0]['kd_hold'] = 3
        parsed_data,answer = f_load_json(Json_setAccount,service) 
        response_answer(answer,error,Json_setAccount,name_test)
        find_error('G2_STG_ACCOUNT','NM_EXCH_KEY',pformat(Json_setAccount['account'][0]['nm_exch_key']),'','', error,name_test,1,Json_setAccount,2)
def setAddrObjDataError(): #тест на апдейт данных по абоненту
    service = 'setAddrObjData'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:     

        name_test = 'ADR0001 Пустой id_fias_guid'
        error = 'ADR0001'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['id_fias_guid'] = ''
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0002'
        error = 'ADR0002'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['id_fias_guid'] = 'd00a58ку-8650-49ff-993f-09f01cd4694c'
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)


        name_test = 'ADR0003'
        error = 'ADR0003'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = None
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0003_2'
        error = 'ADR0003'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 5
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0004'
        error = 'ADR0004'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nm_oktmo'] = ''
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0004_2 Некор'
        error = 'ADR0004'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nm_oktmo'] = '123456789012'
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0005'
        error = 'ADR0005'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nm_postcode'] = ''
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0005_2'
        error = 'ADR0005'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nm_postcode'] = '1234567'
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0006'
        error = 'ADR0006'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['kd_houses_same_address'] = 1
        Json_setAddrObjData['address_object'][0]['nn_house_type'] = 2
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0024'
        error = 'ADR0024'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['nm_exch_key'] = ''
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)

        name_test = 'ADR0025'
        error = 'ADR0025'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        Json_setAddrObjData['address_object'][0]['dt_actual'] = ''
        parsed_data,answer = f_load_json(Json_setAddrObjData,service)
        response_answer(answer,error,Json_setAddrObjData,name_test)
        find_error('G2_STG_ADDRESS_OBJECT','ID_FIAS_GUID',pformat(Json_setAddrObjData['address_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setAddrObjData)
def setChargeDocumentError(): #тест на апдейт данных по абоненту
    service = 'setChargeDocument'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:    
       
        name_test = 'PD0001'
        error = 'PD0001'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['nm_exch_key'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        #Проверка
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)

        name_test = 'PD0002'
        error = 'PD0002'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['dt_actual'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)

        name_test = 'PD0003'
        error = 'PD0003'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['id_charge_document'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0004'
        error = 'PD0004'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['id_account'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0005'
        error = 'PD0005'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['nm_account'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0006'
        error = 'PD0006'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['dt_charge'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        # name_test = 'PD0007' не сделано
        # error = 'PD0007'
        # Json_setChargeDocument = generation_ChargeDocument()
        # Json_setChargeDocument['charge_document'][0]['dt_charge'] = ''
        # parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        # response_answer(answer,error,Json_setChargeDocument,name_test)

        name_test = 'PD0008'
        error = 'PD0008'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['nm_org_pu_uuid'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)    
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0008_1'
        error = 'PD0008'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['nm_org_pu_uuid'] = 'ed4e0da8-65f1-4cbf-83a3-110fae2f83ec'
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test) 
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)
 

        name_test = 'PD0012'
        error = 'PD0012'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = None
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0012_1'
        error = 'PD0012'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 11
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0013'
        error = 'PD0013'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE','NULL', error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0013_2'
        error = 'PD0013'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 2
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '8'
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0013_3'
        error = 'PD0013'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 4
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '14'
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0013_4'
        error = 'PD0013'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 5
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '9'
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0013_5'
        error = 'PD0013'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 6
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'] = '2'
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0015'
        error = 'PD0015'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_service_type'] = 3
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_tariff'] = None
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0016'
        error = 'PD0016'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_total_accrued'] = None
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0017'
        error = 'PD0017'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_total_pay'] = None
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0018'
        error = 'PD0018'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_corr'] = 1.0
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nm_info_corr'] = ''
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0020'
        error = 'PD0020'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_installment'] = 1.0
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_rate_installment'] = None
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)

        
        name_test = 'PD0020_2'
        error = 'PD0020'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_installment'] = 1.0
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_rate_installment'] = 101.0
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)


        name_test = 'PD0021'
        error = 'PD0021'
        wright_txt(str(name_test))
        Json_setChargeDocument = generation_ChargeDocument()
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_installment'] = 1.0
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_rate_installment'] = 1.0
        Json_setChargeDocument['charge_document'][0]['charge_info'][0]['charge'][0]['nn_sum_pay_with_installment_rate'] = None
        parsed_data,answer = f_load_json(Json_setChargeDocument,service)
        response_answer(answer,error,Json_setChargeDocument,name_test)
        find_error('G2_STG_CHARGE_DOCUMENT','ID_CHARGE_DOCUMENT',pformat(parsed_data['charge_document'][0]['id_charge_document']),'NM_SERVICE_CODE',parsed_data['charge_document'][0]['charge_info'][0]['charge'][0]['nm_service_code'], error,name_test,2,Json_setChargeDocument)
def setMeteringDeviceError(): 
    service = 'setMeteringDevice'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:     

        id_fias_guid,id_house_object = created_addr_house('setAccountError')  

        name_test = 'PU0001'
        error = 'PU0001'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['id_metering_device'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0002'
        error = 'PU0002'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = None
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0002'
        error = 'PU0002'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 2
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0002'
        error = 'PU0002'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = -1
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0003'
        error = 'PU0003'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_type_meter'] = None
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0003'
        error = 'PU0003'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_type_meter'] = 4
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)
        
        name_test = 'PU0003'
        error = 'PU0003'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_type_meter'] = -1
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0004'
        error = 'PU0004'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_type_meter'] = 2
        Json_setMeteringDevice['metering_device'][0]['accounts'] = []
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0004'
        error = 'PU0004'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_type_meter'] = 3
        Json_setMeteringDevice['metering_device'][0]['accounts'] = []
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0005'
        error = 'PU0005'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nm_serial_number'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0006'
        error = 'PU0006'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nm_marka'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0007'
        error = 'PU0007'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nm_model'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0008'
        error = 'PU0008'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_installation'] = '0001-01-01T25:61:62'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0008'
        error = 'PU0008'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_installation'] = '123654785'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0008'
        error = 'PU0008'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_installation'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0009'
        error = 'PU0009'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_commissioned'] = '0001-01-01T25:61:62'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0009'
        error = 'PU0009'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_commissioned'] = '123654785'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0009'
        error = 'PU0009'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_commissioned'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0010'
        error = 'PU0010'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_first_verification'] = '0001-01-01T25:61:62'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0010'
        error = 'PU0010'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_first_verification'] = '123654785'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0010'
        error = 'PU0010'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_first_verification'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0011'
        error = 'PU0011'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_seal'] = '0001-01-01T25:61:62'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0011'
        error = 'PU0011'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_seal'] = '123654785'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0011'
        error = 'PU0011'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_seal'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0012'
        error = 'PU0012'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['id_verification_interval'] = None
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0012'
        error = 'PU0012'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['id_verification_interval'] = -2
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0013'
        error = 'PU0013'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_consumed_volume'] = None
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0013'
        error = 'PU0013'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_consumed_volume'] = -1
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0013'
        error = 'PU0013'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_consumed_volume'] = 2
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0014'
        error = 'PU0014'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['id_municipal_resource_type'] = None
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0014'
        error = 'PU0014'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['id_municipal_resource_type'] = "-2"
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0015'
        error = 'PU0015'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = None
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0015'
        error = 'PU0015'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0015'
        error = 'PU0015'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_tarif'] = 4
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0016'
        error = 'PU0016'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = None
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0016'
        error = 'PU0016'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0016'
        error = 'PU0016'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 3
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

    #--------------------------
        name_test = 'PU0017'
        error = 'PU0017'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 1
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0017'
        error = 'PU0017'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 1
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0018'
        error = 'PU0018'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 1
        Json_setMeteringDevice['metering_device'][0]['id_archiving_reason'] = None
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0018'
        error = 'PU0018'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 1
        Json_setMeteringDevice['metering_device'][0]['id_archiving_reason'] = -2
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0019'
        error = 'PU0019'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2
        Json_setMeteringDevice['metering_device'][0]['kd_planned_verification'] = None
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0019'
        error = 'PU0019'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2
        Json_setMeteringDevice['metering_device'][0]['kd_planned_verification'] = -1
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0019'
        error = 'PU0019'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2
        Json_setMeteringDevice['metering_device'][0]['kd_planned_verification'] = 2
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0020'
        error = 'PU0020'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2
        Json_setMeteringDevice['metering_device'][0]['id_metering_device_replace'] = ''
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0021'
        error = 'PU0021'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['id_metering_device_replace'] = '4523'
        Json_setMeteringDevice['metering_device'][0]['kd_status'] = 0
        Json_setMeteringDevice['metering_device'][0]['nn_archiving_type'] = 2        
        Json_setMeteringDevice['metering_device'][0]['kd_planned_verification'] = 0
        Json_setMeteringDevice['metering_device'][0]['id_failure_reason'] = None

        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------

        name_test = 'PU0022'
        error = 'PU0022'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['address_object'][0]['id_fias_guid'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0022_2'
        error = 'PU0022'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['address_object'][0]['id_fias_guid'] = 'РНГДaada30b33d064a1da5ef87deed37720f'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0029'
        error = 'PU0029'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['nm_exch_key'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        #--------------------------
        name_test = 'PU0030'
        error = 'PU0030'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_actual'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0030'
        error = 'PU0030'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_actual'] = '0001-01-01T25:61:62'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)

        name_test = 'PU0030'
        error = 'PU0030'
        wright_txt(str(name_test))
        Json_setMeteringDevice = generation_MeteringDevice(id_fias_guid)
        #Условие
        Json_setMeteringDevice['metering_device'][0]['dt_actual'] = '4235456876'
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDevice,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDevice,name_test)
        find_error('G2_STG_METERING_DEVICE','ID_METERING_DEVICE',pformat(parsed_data['metering_device'][0]['id_metering_device']),'','', error,name_test,1,Json_setMeteringDevice)
def setMeteringDeviceValueError(): 
    service = 'setMeteringDeviceValues'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:    
       
        name_test = 'PPU0001'
        error = 'PPU0001'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        #Условие
        Json_setMeteringDV['metering_device_values'][0]['id_metering_device'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        #Проверка
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0002'
        error = 'PPU0002'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['id_metering_device_values'] = ''
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0003'
        error = 'PPU0003'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = None
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0003_2'
        error = 'PPU0003'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 4
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0004'
        error = 'PPU0004'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['dt_indication'] = ''
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0005'
        error = 'PPU0005'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 2
        Json_setMeteringDV['metering_device_values'][0]['dt_start_verification'] = ''
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0005_2'
        error = 'PPU0005'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 3
        Json_setMeteringDV['metering_device_values'][0]['dt_start_verification'] = ''
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0006'
        error = 'PPU0006'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 3
        Json_setMeteringDV['metering_device_values'][0]['dt_start_verification'] = '2012-02-10T00:00:00'
        Json_setMeteringDV['metering_device_values'][0]['dt_end_verification'] = ''
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0007'
        error = 'PPU0007'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 3
        Json_setMeteringDV['metering_device_values'][0]['dt_start_verification'] = '2012-02-10T00:00:00'
        Json_setMeteringDV['metering_device_values'][0]['dt_end_verification'] = '2020-02-10T00:00:00'
        Json_setMeteringDV['metering_device_values'][0]['id_failure_reason'] = None
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0007_2'
        error = 'PPU0007'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_type_indication'] = 3
        Json_setMeteringDV['metering_device_values'][0]['dt_start_verification'] = '2012-02-10T00:00:00'
        Json_setMeteringDV['metering_device_values'][0]['dt_end_verification'] = '2020-02-10T00:00:00'
        Json_setMeteringDV['metering_device_values'][0]['id_failure_reason'] = 6
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0008'
        error = 'PPU0008'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nm_exch_key'] = ''
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0009'
        error = 'PPU0009'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['dt_actual'] = ''
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)

        name_test = 'PPU0010'
        error = 'PPU0010'
        wright_txt(str(name_test))
        Json_setMeteringDV = generation_MeteringDV()
        Json_setMeteringDV['metering_device_values'][0]['nn_value_1'] = None
        Json_setMeteringDV['metering_device_values'][0]['nn_value_2'] = None
        Json_setMeteringDV['metering_device_values'][0]['nn_value_3'] = None
        parsed_data,answer = f_load_json(Json_setMeteringDV,service)
        response_answer(answer,error,Json_setMeteringDV,name_test)
        find_error('G2_STG_METERING_DEVICE_VALUE','ID_METERING_DEVICE_VALUE',pformat(parsed_data['metering_device_values'][0]['id_metering_device_values']),'','', error,name_test,1,Json_setMeteringDV)
def setContractError(): 
    service = 'setContract'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:     

        id_fias_guid,id_house_object = created_addr_house('setAccountError')  

        name_test = 'DOG0001'
        error = 'DOG0001'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        #Условие
        Json_setContract['contracts'][0]['id_contract'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setContract,service)
        #Проверка
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0002'
        error = 'DOG0002'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['nn_open'] = None
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0002_2'
        error = 'DOG0002'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['nn_open'] = 5
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0003'
        error = 'DOG0003'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['dt_signing'] = ''
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0004'
        error = 'DOG0004'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 1
        Json_setContract['contracts'][0]['nn_type_owner'] = None
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0004_2'
        error = 'DOG0004'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = None
        Json_setContract['contracts'][0]['nn_type_owner'] = 1
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0004_3'
        error = 'DOG0004'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 1
        Json_setContract['contracts'][0]['nn_type_owner'] = 6
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0004_4'
        error = 'DOG0004'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 6
        Json_setContract['contracts'][0]['nn_type_owner'] = 1
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0005'
        error = 'DOG0005'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 1
        Json_setContract['contracts'][0]['id_identity_document'] = 1
        Json_setContract['contracts'][0]['nm_number_identity_document'] = ''
        Json_setContract['contracts'][0]['dt_identity_document'] = '2020-06-02T10:31:02'
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0005_2'
        error = 'DOG0005'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 1
        Json_setContract['contracts'][0]['id_identity_document'] = 1
        Json_setContract['contracts'][0]['nm_number_identity_document'] = '425343243'
        Json_setContract['contracts'][0]['dt_identity_document'] = ''
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0006'
        error = 'DOG0006'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 2
        Json_setContract['contracts'][0]['nn_state_reg_number'] = None
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0006_2'
        error = 'DOG0006'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 2
        Json_setContract['contracts'][0]['nn_state_reg_number'] = 1234
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0006_3'
        error = 'DOG0006'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 3
        Json_setContract['contracts'][0]['nn_state_reg_number'] = None
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0006_4'
        error = 'DOG0006'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 3
        Json_setContract['contracts'][0]['nn_state_reg_number'] = 1234
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0006_5'
        error = 'DOG0006'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 4
        Json_setContract['contracts'][0]['nn_state_reg_number'] = None
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0006_6'
        error = 'DOG0006'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['kd_offer'] = 0
        Json_setContract['contracts'][0]['nn_owner'] = 2
        Json_setContract['contracts'][0]['nn_type_owner'] = 4
        Json_setContract['contracts'][0]['nn_state_reg_number'] = 1234
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0007'
        error = 'DOG0007'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['nn_billing_date'] = None
        Json_setContract['contracts'][0]['kd_billing_month'] = 0
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0007_2'
        error = 'DOG0007'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['nn_billing_date'] = None
        Json_setContract['contracts'][0]['kd_billing_month'] = None
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0008'
        error = 'DOG0008'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['contract_subject'] = []
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0009'
        error = 'DOG0009'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['contract_subject'][0]['id_municipal_resource'] = 999
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0010'
        error = 'DOG0010'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['contract_subject'][0]['id_service_type'] = "999"
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0011'
        error = 'DOG0011'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_start_resource'] = ''
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0012'
        error = 'DOG0012'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['address_object'] = []
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0012_2'
        error = 'DOG0012'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['address_object'][0]['id_fias_guid'] = ''
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0018'
        error = 'DOG0018'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['dt_end'] = '2020-04-27T00:00:00'
        Json_setContract['contracts'][0]['kd_prolongation'] = 0
        Json_setContract['contracts'][0]['contract_subject'][0]['dt_end_resource'] = ''
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0019'
        error = 'DOG0019'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['nn_open'] = 2
        Json_setContract['contracts'][0]['dt_terminate'] = ''
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)

        name_test = 'DOG0020'
        error = 'DOG0020'
        wright_txt(str(name_test))
        Json_setContract = generation_Contract(id_fias_guid)
        Json_setContract['contracts'][0]['nn_open'] = 3
        Json_setContract['contracts'][0]['dt_rollover_end'] = ''
        parsed_data,answer = f_load_json(Json_setContract,service)
        response_answer(answer,error,Json_setContract,name_test)
        find_error('G2_STG_CONTRACT','ID_CONTRACT',pformat(parsed_data['contracts'][0]['id_contract']),'','', error,name_test,1,Json_setContract)
def setPaymentsError(): 
    service = 'setPayments'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:    
        
        name_test = 'PAY0001'
        error = 'PAY0001'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        #Условие
        Json_setPayments['payments'][0]['id_payment'] = ''
        #Отправка
        parsed_data,answer = f_load_json(Json_setPayments,service)
        #Проверка
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)

        name_test = 'PAY0002'
        error = 'PAY0002'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['id_account'] = ''
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)

        name_test = 'PAY0003'
        error = 'PAY0003'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['dt_pay'] = ''
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)

        name_test = 'PAY0004'
        error = 'PAY0004'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['dt_period'] = ''
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)

        name_test = 'PAY0005'
        error = 'PAY0005'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['id_ipd'] = ''
        Json_setPayments['payments'][0]['id_zhku'] = ''
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)

        name_test = 'PAY0006'
        error = 'PAY0006'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['nn_sm_pay'] = 0
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)

        name_test = 'PAY0007'
        error = 'PAY0007'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['kd_cancel'] = 1
        Json_setPayments['payments'][0]['dt_pay_cancel'] = ''
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)

        name_test = 'PAY0008'
        error = 'PAY0008'
        wright_txt(str(name_test))
        Json_setPayments = generation_Payments()
        Json_setPayments['payments'][0]['nm_exch_key'] = ''
        parsed_data,answer = f_load_json(Json_setPayments,service)
        response_answer(answer,error,Json_setPayments,name_test)
        find_error('G2_STG_PAYMENT','ID_PAYMENT',pformat(parsed_data['payments'][0]['id_payment']),'','', error,name_test,1,Json_setPayments)
def setHouseObjDataError(): #тест на апдейт данных по абоненту
    service = 'setHouseObjData'
    if type_of_test == 2 or type_of_test == 3 and load_json == 1:   

        name_test = 'HO0001'
        error = 'HO0001'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['id_fias_guid'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result'])=='CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
        
        name_test = 'HO0002'
        error = 'HO0002'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 9
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result'])=='CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0003'
        error = 'HO0003'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 1
        Json_setHouseObjData['house_object'][0]['nm_entrance'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result'])=='CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0004'
        error = 'HO0004'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 2
        Json_setHouseObjData['house_object'][0]['nm_block'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0004_2'
        error = 'HO0004'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 3
        Json_setHouseObjData['house_object'][0]['nm_block'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0005'
        error = 'HO0005'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 4
        Json_setHouseObjData['house_object'][0]['nm_premises'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0005_2'
        error = 'HO0005'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 5
        Json_setHouseObjData['house_object'][0]['nm_premises'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0006'
        error = 'HO0006'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 8
        Json_setHouseObjData['house_object'][0]['nm_block'] = '4'
        Json_setHouseObjData['house_object'][0]['nm_room'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0006_2'
        error = 'HO0006'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 6
        Json_setHouseObjData['house_object'][0]['nm_room'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0006_3'
        error = 'HO0006'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 7
        Json_setHouseObjData['house_object'][0]['nm_room'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0007'
        error = 'HO0007'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 6
        Json_setHouseObjData['house_object'][0]['nm_room'] = '6'
        Json_setHouseObjData['house_object'][0]['nm_premises'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)


        name_test = 'HO0008'
        error = 'HO0008'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nn_type_object'] = 8   
        Json_setHouseObjData['house_object'][0]['nm_block'] = ''
        Json_setHouseObjData['house_object'][0]['nm_room'] = '6'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0009'
        error = 'HO0009'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['id_reasons_cancell'] = 99   
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0010'
        error = 'HO0010'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['nm_exch_key'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0011'
        error = 'НО0011'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['dt_actual'] = ''
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)

        name_test = 'HO0011_2'
        error = 'НО0011'
        wright_txt(str(name_test))
        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        Json_setHouseObjData['house_object'][0]['dt_actual'] = '2019-10-02Tr12:01:12'
        parsed_data_1,answer_1 = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json = answer_1.json()
        if (answer_json['nm_result']) == 'CREATED':
            parsed_data,answer = f_load_json(Json_setHouseObjData,service)
            response_answer(answer,error,Json_setHouseObjData,name_test)
            find_error('G2_STG_HOUSE_OBJECT','ID_FIAS_GUID',pformat(parsed_data['house_object'][0]['id_fias_guid']),'','', error,name_test,1,Json_setHouseObjData)
        else:
            wright_txt('Не создался адресный объект. '+name_test)


# -----------Функции--------------------------------------------------------
#запрос id организации по uuid
def f_org(nm_org_uuid): 
    nm_org_uuid = (pformat(nm_org_uuid))
    jat_orgs_table = rbd_conn.execute("select o.id_org from jat_orgs o where o.nm_org_uuid = "+nm_org_uuid+"")
    jat_orgs_mas = jat_orgs_table.fetchall() 
    orgs_dl = len(jat_orgs_mas)
    if orgs_dl == 0:
        wright_txt('При запросе организации по nm_org_uuid = '+nm_org_uuid+' организация не найдена в БД.')
        error = error+1
    else:
        id_org = int(jat_orgs_mas[0]['id_org'])
        return(id_org)
#запрос данных абонента по ЛС
def f_find_account(id_account): #запрос данных абонента по ЛС
        jt_account_table = rbd_conn.execute("""select 
                                                        acc.nm_exch_key,
                                                        acc.dt_actual,
                                                        acc.nm_org_uuid,
                                                        acc.id_account,
                                                        acc.nm_account,
                                                        acc.kd_open,
                                                        acc.id_fias_guid,
                                                        acc.nn_living_people_number,
                                                        acc.nn_total_area,
                                                        acc.nn_residential_area,
                                                        acc.nn_heated_area,
                                                        acc.dt_close,
                                                        acc.id_close_reason,
                                                        acc.nn_own_percent,
                                                        acc.nn_type_owner,
                                                        acc.nm_surname,
                                                        acc.nm_name,
                                                        acc.nm_middle_name,
                                                        acc.nm_sex,
                                                        acc.dt_date_birth,
                                                        acc.id_identity_document,
                                                        acc.nm_serial_identity_document,
                                                        acc.nm_number_identity_document,
                                                        acc.dt_identity_document,
                                                        acc.nm_snils,
                                                        acc.nn_state_reg_number,
                                                        acc.kd_hold,
                                                        acc.nm_transport_uuid,
                                                        acc.nm_error_code,
                                                        acc.nm_error_description,
                                                        acc.load_id,
                                                        acc.is_valid 
                                                        from g2_stg_account acc 
                                                        where acc.id_account = """+id_account+"")
        jt_account_table_mas = jt_account_table.fetchall()
        return(jt_account_table_mas)
# Функция подсчета коллиства записей в таблице с уловием  WHERE "+field+" ="+value+"
# Вход: название таблицы, название поля для условия, значение для поиска
def f_count(table,field,value): #функция подсчета 
    time.sleep(0.1)
    sql_count = "select count(*) count FROM "+table+" WHERE "+field+" ="+value+""
    jat_counters_indication_count = rbd_conn.execute(sql_count)
    jat_counters_indication_masc = jat_counters_indication_count.fetchall()   
    count = (jat_counters_indication_masc[0]['count'])
    return(count)
# Функция подсчета коллиства записей в таблице с уловием  WHERE "+field+" ="+value+"
# Вход: название таблицы, название поля для условия, значение для поиска
def f_count_2field(table,field1,value1,field2,value2): #функция подсчета 
    jat_counters_indication_count = rbd_conn.execute("select count(*) count FROM "+table+" WHERE "+field1+" ="+value1+" and "+field2+" ="+value2+"")
    jat_counters_indication_masc = jat_counters_indication_count.fetchall()   
    count = (jat_counters_indication_masc[0]['count'])
    return(count)
# Функция получение системного времени с сервера БД
def f_sysdate(): 
        sysdate_table = rbd_conn.execute("select sysdate from dual")
        sysdate_mas = sysdate_table.fetchall()
        sysdate = str(pandas.to_datetime(sysdate_mas[0]['sysdate']))
        sysdate = sysdate [0:13] # обрезаем дату, так как невозможно получить точную до минуты
        return (sysdate)
# Функция отправки json в гис
def f_load_json(file_json,service): #функция отправки json в гис
    headers = {'x-token': settings_json['server']['portal']['authorization']['x_token']} 
    clientCrt = settings_json['server']['portal']['authorization']['clientCrt']
    clientKey = settings_json['server']['portal']['authorization']['clientKey']
    ip_portal = settings_json['server']['portal']['ip']
    application_portal = settings_json['server']['portal']['application']
    url = 'https://'+ip_portal+'/'+application_portal+'/'+service+'' 
    p_json = file_json   
    if load_json == 1:
        answer = requests.post(url, cert=(clientCrt,clientKey), verify=False, json=p_json, headers=headers) 
    if load_json == 0:
        answer = ''
    return(p_json,answer)
# Функция генерации sql запроса с выводом всех полей из таблицы c условие where = field 
# Вход: название таблицы, название поля для условия, значение для поиска
def generation_sql_select(table_name,field,value):
    counter = 0 #Счетчик
    sql_select_colum = '' #Переменная для хранения списка колонок
    #Запрос выбора всех колонок в таблице
    sql_table = rbd_conn.execute("""select column_name 
                                    from all_tab_columns 
                                    where table_name = '"""+table_name+"""'
                                                        """)

    sql_mas = sql_table.fetchall()
    count_colum = len(sql_mas) #Считаем количество колонок
    #Название каждой колонки плюсум к строке с добалением ','
    while counter < count_colum: 
        sql_select_colum = sql_select_colum + str(sql_mas[counter][0]) +','
        counter = counter+1
    #Считаем количество символов в строке -1
    sql_select_colum_len = len(sql_select_colum) - 1
    #Берем всю строку за исключением последнего символа 
    sql_select_colum = (sql_select_colum)[0:sql_select_colum_len] 
    #Формируем запрос
    sql_select_colum = 'select ' +sql_select_colum+ ' from ' +table_name+ ' where ' +field+ '=' +value
    return(sql_select_colum)
# Функция генерации sql запроса с выводом всех полей из таблицы c условие where = по двум field 
# Вход: название таблицы, название поля для условия, значение для поиска, название поля2 для условия, значение для поиска2
def generation_sql_select_2field(table_name,field,value,field2,value2):
    counter = 0 #Счетчик
    sql_select_colum = '' #Переменная для хранения списка колонок
    #Запрос выбора всех колонок в таблице
    sql_table = rbd_conn.execute("""select column_name 
                                    from all_tab_columns 
                                    where table_name = '"""+table_name+"""'
                                                        """)

    sql_mas = sql_table.fetchall()
    count_colum = len(sql_mas) #Считаем количество колонок
    #Название каждой колонки плюсум к строке с добалением ','
    while counter < count_colum: 
        sql_select_colum = sql_select_colum + str(sql_mas[counter][0]) +','
        counter = counter+1
    #Считаем количество символов в строке -1
    sql_select_colum_len = len(sql_select_colum) - 1
    #Берем всю строку за исключением последнего символа 
    sql_select_colum = (sql_select_colum)[0:sql_select_colum_len] 
    #Формируем запрос
    sql_select_colum = 'select ' +sql_select_colum+ ' from ' +table_name+ ' where ' +field+ '=' +value+ ' and ' +field2+ '=' +value2
    return(sql_select_colum)
# Функция сверки данных json и бд
def function_reconciliation(table_value,json_value,info_error):
    table_value = str(table_value).replace(',','.')
    json_value = str(json_value).replace(',','.')
    if json_value == 'NaT':
        json_value = ''    
    if table_value == 'None':
        table_value = ''
    if json_value == 'None':
        json_value = ''
    if json_value != table_value:
        wright_txt(info_error+' '+'json:'+(str)(json_value)+' '+'БД:'+(str)(table_value))
        error='error'
        return(error)  
# Функция анализа ответа (ошибки)    
def response_answer(answer,error,json_file,name_test): 
    if answer.status_code != 200:
        wright_txt('имя теста: '+str(name_test))
        wright_txt('ожидаемый результат: '+str(error))
        wright_txt('код ответа не равен 200. status code = '+str(answer.status_code))
        wright_txt(str(json_file))
    else:
        try:
            answer = answer.json()
        except ValueError:
            wright_txt('имя теста: '+str(name_test))
            wright_txt('ожидаемый результат: '+str(error))
            wright_txt('в ответе отсутствует блок content')
            wright_txt(str(json_file))
            return()
    
    if name_test[:4] == 'Succ':
        if (answer['nm_result'])!='CREATED':
            wright_txt('имя теста: '+str(name_test))
            wright_txt('ожидаемый результат: '+str(error))
            wright_txt('полученный ответ:'+str(answer['errors'][0]['nm_error_code']))
            wright_txt(str(json_file))
    
    else:
        if (answer['nm_result'])!='NOT_VALID':
            wright_txt('имя теста: '+str(name_test))
            wright_txt('ожидаемый результат: '+str(error))
            wright_txt('полученный ответ:'+str(answer['nm_result']))
            wright_txt(str(json_file))
def response_answer_error(answer,error,json_file,name_test): 
    
    
    if answer.status_code != 200:
        wright_txt('имя теста: '+str(name_test))
        wright_txt('ожидаемый результат: '+str(error))
        wright_txt('код ответа не равен 200. status code = '+str(answer.status_code))
        wright_txt(str(json_file))
    else:
        try:
            answer = answer.json()
        except ValueError:
            wright_txt('имя теста: '+str(name_test))
            wright_txt('ожидаемый результат: '+str(error))
            wright_txt('в ответе отсутствует блок content')
            wright_txt(str(json_file))
            return()
    
    if name_test[:4] == 'Succ':
        if (answer['nm_result'])!='CREATED':
            wright_txt('имя теста: '+str(name_test))
            wright_txt('ожидаемый результат: '+str(error))
            wright_txt('полученный ответ:'+str(answer['errors'][0]['nm_error_code']))
            wright_txt(str(json_file))
    
    else:
        if (answer['nm_result'])!='NOT_VALID':
            wright_txt('имя теста: '+str(name_test))
            wright_txt('ожидаемый результат: '+str(error))
            wright_txt('полученный ответ:'+str(answer['errors'][0]['nm_error_code']))
            wright_txt(str(json_file))
    
def find_error(table_name,field,value,field2,value2,error,error_name,count_fild,json,search_table_error):
    #ищем строку в таблице G2_ERROR и проверяем код ошибки
    if field == 'NM_EXCH_KEY':
        field_error = 'NM_EXCH_KEY'
    else:
        field_error = "ID_ENTITY"        
    count = f_count('G2_ERROR',field_error,value)
    if count == 0:
        wright_txt(str('В таблице G2_ERROR не создалась строка. Тест: '+error_name))
    else:
        error_sql = 'select nvl(NM_ERROR_CODE, 0) NM_ERROR_CODE from G2_ERROR where ' +field_error+ '=' +value
        error_table = rbd_conn.execute(""+error_sql+"")
        error_mas = error_table.fetchall()
        if len(error_mas) == 0:
            errorbd = 'Пусто'
        else:
            errorbd = error_mas[0][0]
        if error != errorbd:
            wright_txt(str('Ошибка не соответсвует ожидаемой. Ожидаемый результат: '+error+'. Полученный результат: '+errorbd+'. Тест: '+error_name))
    #ищем строку в основной таблице и проверяем ошибку
    if search_table_error == 2:
        if count_fild == 1:
            count = f_count(table_name,field,value)
        if count_fild == 2:
            count = f_count_2field(table_name,field,value,field2,value2)
        if count == 0:
            
            wright_txt(str('В базе не создалась строка. Тест: '+error_name))
        else:
            if count_fild == 1:
                main_error_sql = 'select nvl(NM_ERROR_CODE, 0) NM_ERROR_CODE from ' +table_name+ ' where ' +field+ '=' +value
            if count_fild == 2:
                main_error_sql = 'select nvl(NM_ERROR_CODE, 0) NM_ERROR_CODE from ' +table_name+ ' where ' +field+ '=' +value+ ' and ' +field2+ '=' +value2
            main_error_table = rbd_conn.execute(""+main_error_sql+"")
            main_error_mas = main_error_table.fetchall()
            if len(main_error_mas) == 0:
                main_errorbd = 'Пусто'
            else:
                main_errorbd = main_error_mas[0][0]
            if error != main_errorbd:
                wright_txt(str('Ошибка не соответсвует ожидаемой. Ожидаемый результат: '+error+'. Полученный результат: '+main_errorbd+'. Тест: '+error_name))

# Функция разбора даты
def parsed_date_time(date_time):
    try:
        date_time = (str(pandas.to_datetime(date_time)))[0:10]
    except ValueError:
        date_time = (str(date_time))[0:10]
    return(date_time)
# Функция создания адреса и дома для тестов
def created_addr_house(name_test):

        Json_setAddrObjData = generation_AddrObjData()
        id_fias_guid = Json_setAddrObjData['address_object'][0]['id_fias_guid']
        Json_setHouseObjData = generation_HouseObjData(id_fias_guid)
        id_house_object = Json_setHouseObjData['house_object'][0]['id_house_object']
        parsed_data_addr,answer_addr = f_load_json(Json_setAddrObjData,'setAddrObjData')
        answer_json_addr = answer_addr.json()
        if (answer_json_addr['nm_result']) == 'CREATED':
            parsed_data_house,answer_house = f_load_json(Json_setHouseObjData,'setHouseObjData')
            answer_json_house = answer_house.json()
            if (answer_json_house['nm_result']) != 'CREATED':
                wright_txt('Не создался дом. '+name_test)
                response_answer(answer_house,'CREATED',Json_setHouseObjData,name_test)
        else:
            wright_txt('Не создался адресный объект. '+name_test)
            response_answer(answer_addr,'CREATED',Json_setAddrObjData,name_test)
        return(id_fias_guid,id_house_object)
# Функция чтения файла json
def read_json(json_file_direct):
    with open(json_file_direct, 'r', encoding="utf-8-sig") as f:
        json_read = json.loads(f.read())   
    return(json_read)
def wright_txt(text):
    file_error.write(text+ '\n')

if __name__ == "__main__":
    # setAddrObjData()
    # setAccount()
    # setMeteringDevice()
    # setMeteringDeviceValues()
    # setChargeDocument()
    # setContract()
    # setPayments()

    setAccountError()
    # setAddrObjDataError()
    # setChargeDocumentError()
    # setMeteringDeviceError()
    # setPaymentsError()
    # setMeteringDeviceValueError()
    # setContractError()
    # setHouseObjDataError()
    
    # setAccountSuccessfully()
    # setAddrObjDataSuccessfully()
    # setChargeDocumentSuccessfully()
    # setMeteringDeviceSuccessfully()
    # setMeteringDeviceValueSuccessfully()
    # setContractSuccessfully()
    # setPaymentsSuccessfully()
    # setHouseObjDataSuccessfully()
