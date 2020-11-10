import sqlalchemy as alch 
import cx_Oracle 
import requests
import json
import ast
import pandas
import warnings
import random
import datetime
import re
import timeit
import time
import threading
from pprint import pprint, pformat
from pathlib import Path
import progressbar

def f_mas_info():
    #info
    mas_info = [[0 for j in range(1)] for i in range(7)]
    mas_info [0][0] = 'ЗАО Газпром межрегионгаз Кемерово'           #nm_org_name
    mas_info [1][0] = 'ed5e0da8-65f1-4cbf-83a3-110fae2f83ec'        #nm_org_uuid
    mas_info [2][0] = '116872602119474238986410386619251945532'     #nn_batch_serial
    mas_info [3][0] = '2019-01-01T00:00:00'                         #dt_report_period
    mas_info [4][0] = '1'                                           #nn_current_page
    mas_info [5][0] = '1'                                           #nn_total_pages
    mas_info [6][0] = '1.01'                                        #nm_version
    return(mas_info)
def f_mas_setAccount():
    #setAccount
    mas_setAccount = [[0 for j in range(1)] for i in range(38)]
    #account



    mas_setAccount [19][0] = '1978-12-22T00:00:00'                  #dt_date_birth
    mas_setAccount [20][0] = '1'                                    #id_identity_document
    mas_setAccount [21][0] = '12 02'                                #nm_serial_identity_document
    mas_setAccount [22][0] = '369569'                               #nm_number_identity_document
    mas_setAccount [23][0] = '2002-02-25T00:00:00'                  #dt_identity_document
    mas_setAccount [24][0] = '643535345'                            #nm_snils
    mas_setAccount [25][0] = '573456345'                            #nn_state_reg_number
    mas_setAccount [26][0] = '0'                                    #kd_hold
    #contracts
    mas_setAccount [27][0] = '6146545654'                           #id_contract
    #house_object
    mas_setAccount [28][0] = 'd00a58ae-8650-49ff-993f-09f01cd4694c' #id_fias_guid
    mas_setAccount [29][0] = '2019-10-02T12:01:12'                  #dt_actual
    mas_setAccount [30][0] = '4'                                    #nn_type_object
    mas_setAccount [31][0] = ''                                     #id_fias_guid_parent
    mas_setAccount [32][0] = '1'                                    #nm_entrance
    mas_setAccount [33][0] = '8'                                    #nm_block
    mas_setAccount [34][0] = '1'                                    #nm_premises
    mas_setAccount [35][0] = '89'                                   #nm_room
    mas_setAccount [36][0] = '66.3'                                 #nn_total_area
    mas_setAccount [37][0] = '0'                                    #id_reasons_cancell
    return(mas_setAccount)

def Generation_Info_json(bloc):#заполняем структуру json из масива 
    sysdate = datetime.datetime.now()
    dt_report_period = str(pandas.to_datetime((str(sysdate.year))+'-'+(str(sysdate.month))+'-'+(str(sysdate.day)),format='%Y/%m/%d')).replace(" ", "T")   
    Json_info = { 
    "info":{ 
        "nm_org_name":'ЗАО Газпром межрегионгаз Кемерово',
        "nm_org_uuid":'ed5e0da8-65f1-4cbf-83a3-110fae2f83ec',
        "nn_batch_serial":'116872602119474238986410386619251945532',
        "dt_report_period":dt_report_period,
        "nn_current_page":1,
        "nn_total_pages":1,
        "nm_version":'1.01'
    },
    ""+bloc+"""""":[]
    }
    return(Json_info)
def Random():
    list_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
    number = str(random.choice(list_number))
    return(number)
def Random_number():
    list_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number = str(random.choice(list_number))
    return(number)
def Generation_guid():
    time.sleep(0.000001)
    time2 = datetime.datetime.now()
    bloc1 = '002'
    bloc2 = (str(time2.year))
    bloc3 = (str(time2.day))+(str(time2.month))
    bloc4 = (str(time2.hour))+(str(time2.minute))
    bloc5 = (str(time2.second))+(str(time2.microsecond))
    while len(bloc1)<8:
        bloc1 = bloc1+Random()
    while len(bloc2)<4:
        bloc2 = bloc2+Random()
    while len(bloc3)<4:
        bloc3 = bloc3+Random()
    while len(bloc4)<4:
        bloc4 = bloc4+Random()
    while len(bloc5)<12:
        bloc5 = bloc5+Random()
    guid = bloc1+'-'+bloc2+'-'+bloc3+'-'+bloc4+'-'+bloc5
    return(guid)
def Generation_number(size):
    time.sleep(0.000001)
    time2 = datetime.datetime.now()
    if size<17:
        number = '1'
    else:
        number = ((str(time2.year))+(str(time2.day))+(str(time2.month))+(str(time2.hour))+(str(time2.minute))+(str(time2.second))+(str(time2.microsecond)))[0:17]
    while len(number)<size:
        number = number+Random_number()
    number = int(number)
    return(number)
def Generation_string(size):
    time.sleep(0.000001)
    time2 = datetime.datetime.now()
    if size<17:
        number = '1'
    else:
        number = ((str(time2.year))+(str(time2.day))+(str(time2.month))+(str(time2.hour))+(str(time2.minute))+(str(time2.second))+(str(time2.microsecond)))[0:17]
    while len(number)<size:
        number = number+Random()
    return(number)


def setMeteringDVJ():
    Json_MeteringDV = Generation_Info_json('metering_device_values')
    Json_MeteringDV['metering_device_values'].append({  
            "nm_exch_key":'GIS_TEST'+Generation_string(42),
            "dt_actual":'2020-02-17T17:04:00',
            "id_metering_device":Generation_string(36),
            "id_metering_device_values":Generation_string(36),
            "nn_type_indication":1,
            "dt_indication":'2020-01-17T17:04:00',
            "nn_value_1":15.1,
            "nn_value_2":15.2,
            "nn_value_3":15.3,
            "dt_start_verification":'2019-02-17T17:04:00',
            "dt_end_verification":'2023-02-17T17:04:00',
            "dt_seal":'2019-02-17T17:04:00',
            "nn_start_value_verification_1":10.1,
            "nn_start_value_verification_2":10.2,
            "nn_start_value_verification_3":10.3,
            "kd_planned_verification":None,
            "id_failure_reason":None
        })
    return(Json_MeteringDV)
def setMeteringDeviceJ(id_fias_guid):
    Json_MeteringDevice = Generation_Info_json('metering_device')
    Json_MeteringDevice['metering_device'].append({       
            "nm_exch_key":'GIS_TEST'+Generation_string(42),
            "dt_actual":'2019-02-17T17:04:00',
            "id_metering_device":Generation_string(36),
            "kd_status":1,
            "nn_type_meter":2,
            "accounts":[ 
                { 
                "id_account":Generation_string(36)
                }
            ],
            "nm_serial_number":Generation_string(20),
            "nm_marka":Generation_string(50),
            "nm_model":Generation_string(50),
            "dt_installation":'2018-09-17T00:00:00',
            "dt_commissioned":'2018-09-17T00:00:00',
            "kd_remote_measuring":1,
            "nm_remote_system":Generation_string(200),
            "dt_first_verification":'2020-09-17T00:00:00',
            "id_verification_interval":5,
            "dt_seal":'2018-09-17T00:00:00',
            "kd_temperature_sensor":1,
            "nm_temperature_sensor_info":Generation_string(300),
            "kd_pressure_sensor":1,
            "nm_pressure_sensor_info":Generation_string(300),
            "kd_consumed_volume":0,
            "id_municipal_resource_type":'4',
            "id_unit":133,
            "nn_connection_type":1,
            "nn_tarif":1,
            "nn_value_1":1.22,
            "nn_value_arhive_1":1.23,
            "nn_value_2":1.24,
            "nn_value_arhive_2":1.25,
            "nn_value_3":1.26,
            "nn_value_arhive_3":1.27,
            "nn_transformation_ratio":1.5,
            "linked_metering_device":[ 

            ],
            "nn_archiving_type":0,
            "id_archiving_reason":1,
            "kd_planned_verification":1,
            "id_failure_reason":1,
            "id_metering_device_replace":Generation_string(36),
            "address_object":[{
                        "id_fias_guid":id_fias_guid,
                        "house_object":[]
                    }
                ]

        })

    return(Json_MeteringDevice)
def setAccountJ(id_fias_guid, id_house_object): #формирование json setAccount
    Json_setAccount = Generation_Info_json('account')
    time = datetime.datetime.now()
    guid = Generation_guid()
    Json_setAccount['account'].append({ 
            "nm_exch_key":'GIS_TEST'+Generation_string(42),
            "dt_actual":'2018-10-17T12:01:13',
            "id_account":str(Generation_string(36)),
            "nm_account":str(Generation_string(20)),
            "kd_open":1,
            "nn_living_people_number":int(Generation_number(2)),
            "nn_total_area":52.4,
            "nn_residential_area":52.4,
            "nn_heated_area":52.4,
            "dt_close":'',
            "id_closing_reason":0,
            "nn_own_percent":100,
            "nn_type_owner":1,
            "nm_surname":str(Generation_string(100)),
            "nm_name":str(Generation_string(100)),
            "nm_middle_name":str(Generation_string(100)),
            "nm_sex":'М',
            "dt_date_birth":'1978-12-22T00:00:00',
            "id_identity_document":979,
            "nm_serial_identity_document":str(Generation_string(10)),
            "nm_number_identity_document":str(Generation_string(10)),
            "dt_identity_document":'1998-12-22T00:00:00',
            "nm_snils":str(Generation_string(14)),
            "nn_state_reg_number":int(Generation_number(15)),
            "kd_hold":0,
            "contracts":[ 
                { 
                "id_contract":str(Generation_string(36))
                }
            ],
            "address_object": [{
                    "id_fias_guid":id_fias_guid,
                    "nn_own_percent_house": None,
                    "house_object": [{
                        "id_house_object":id_house_object,
                        "nn_own_percent": None
                        }
                    ]
                                    }
                                ]

        })
   
    jsonData = Json_setAccount
    return(Json_setAccount)
def setChargeDocumentJ():
    Json_ChargeDocument = Generation_Info_json('charge_document')
    Json_ChargeDocument['charge_document'].append({   
            "nm_exch_key":'GIS_TEST'+Generation_string(42),
            "dt_actual":'2019-02-17T17:04:00',
            "id_charge_document":Generation_string(36),
            "id_account":Generation_string(36),
            "nm_account":Generation_string(20),
            "id_charge_document_correct":'',
            "kd_cancel":0,
            "dt_charge":'2019-02-17T17:04:00',
            "nn_debt_previous":20.10,
            "nn_advance_previous":21.10,
            "nn_total_sum":22.10,
            "nn_total_sum_pd":23.10,
            "nn_pay_till":31,
            "nn_pay_enter":25.10,
            "dt_pay_enter":'2019-02-17T17:04:00',
            "charge_info":[ 
                { 
                "nm_org_pu_uuid":Json_ChargeDocument['info']['nm_org_uuid'],
                "nm_bank_bik":str(Generation_number(9)),
                "nm_operating_account_number":str(Generation_number(20)),
                "charge":[ 
                    { 
                        "nm_service_code":'1',
                        "nn_service_type":2,
                        "nn_tariff":5.6,
                        "nm_norm":13.10,
                        "id_unit":113,
                        "nn_volume_individ":15.30,
                        "nn_volume_odn":16.30,
                        "nn_boost_coef":17.30,
                        "nn_boost_coef_limit":18.30,
                        "nn_total_accrued":19.30,
                        "nn_sum_privilege":20.30,
                        "nn_sum_corr":21.30,
                        "nm_info_corr":Generation_string(200),
                        "nn_rate_installment":41.30,
                        "nn_sum_installment":31.30,
                        "nn_sum_pay_with_installment_rate":71.30,
                        "nn_total_pay":200.45
                    }
                ]
                }
            ]
        })
    return(Json_ChargeDocument)
def setAddrObjDataJ():
    guid = Generation_guid()
    Json_AddrObjData = Generation_Info_json('address_object')
    Json_AddrObjData['address_object'].append({ 
            "nm_exch_key":'GIS_TEST'+Generation_string(42),
            "dt_actual":'2019-10-02T12:01:12',
            "nn_house_type":1,
            "id_fias_guid":guid,
            "nm_oktmo":Generation_string(11),
            "kd_houses_same_address":0,
            "nm_postcode":str(Generation_number(6)),
            "nm_region":Generation_string(150),
            "nm_autonomic_region":Generation_string(150),
            "nm_district":Generation_string(150),
            "nm_city":Generation_string(150),
            "nm_intracity_district":Generation_string(150),
            "nm_place":Generation_string(150),
            "nm_planning_structure":Generation_string(150),
            "nm_street":Generation_string(120),
            "nm_house_number":str(Generation_number(10)),
            "nm_build_number":str(Generation_number(10)),
            "nm_structure_number":str(Generation_number(10))
    })
    return(Json_AddrObjData)
def setHouseObjDataJ(id_fias_guid):
    Json_HouseObjData = Generation_Info_json('house_object')
    Json_HouseObjData['house_object'].append({ 
            "nm_exch_key":'GIS_TEST'+Generation_string(42),
            "id_house_object":Generation_guid(),
            "id_fias_guid":id_fias_guid,
            "dt_actual":'2019-10-02T12:01:12',
            "nn_type_object":4,
            "id_fias_guid_parent":'',
            "nm_entrance":Generation_string(5),
            "nm_block":'',
            "nm_premises":Generation_string(10),
            "nm_room":'',
            "nn_total_area":33.1,
            "id_reasons_cancell":None,
            "nm_address_full":Generation_string(50)
            })
    return(Json_HouseObjData)
def setPaymentsJ():
    Json_setPayments = Generation_Info_json('payments')
    Json_setPayments['payments'].append({    
         "nm_exch_key":'GIS_TEST'+Generation_string(42),
         "id_payment":Generation_string(36),
         "id_account":Generation_string(36),
         "nm_account":Generation_string(20),
         "kd_correct":0,
         "kd_cancel":0,
         "dt_pay":'2020-06-02T10:31:06',
         "dt_period":'2020-06-02T10:31:06',
         "id_ipd":Generation_string(18),
         "id_zhku":Generation_string(13),
         "nn_sm_pay":22.4,
         "nn_sm_pay_prev":23.4,
         "dt_pay_cancel":''
        })     
    return(Json_setPayments)
def setContractJ(id_fias_guid):
    Json_setContract = Generation_Info_json('contracts')
    Json_setContract['contracts'].append({ 
         "nm_exch_key":'GIS_TEST'+Generation_string(42),
         "dt_actual":'2020-06-02T10:31:02',
         "nm_org_rso_uuid":Generation_guid(),
         "id_contract":Generation_string(36),
         "nm_contract":Generation_string(25),
         "nn_open":1,
         "dt_signing":'1999-01-01T00:00:00',
         "dt_start":'2012-04-27T00:00:00',
         "dt_end":'2022-01-01T00:00:00',
         "kd_prolongation":0,
         "nn_start_counters_indication":21,
         "nn_end_counters_indication":29,
         "kd_next_month_counters_indication":0,
         "kd_offer":1,
         "nn_owner":1,
         "nn_type_owner":1,
         "nm_surname":Generation_string(100),
         "nm_name":Generation_string(100),
         "nm_middle_name":Generation_string(100),
         "nm_sex":'М',
         "dt_date_birth":'1989-01-01T00:00:00',
         "id_identity_document":Generation_number(2),
         "nm_serial_identity_document":Generation_string(10),
         "nm_number_identity_document":Generation_string(10),
         "dt_identity_document":'2002-01-01T00:00:00',
         "nm_snils":Generation_string(14),
         "nn_state_reg_number":2,
         "kd_charge_side":0,
         "kd_counter_side":0,
         "nn_billing_date":29,
         "kd_billing_month":0,
         "nn_payment_date":30,
         "kd_payment_month":0,
         "kd_volume_depends":1,
         "dt_terminate":'2001-01-01T00:00:00',
         "id_termination_reason": 0,
         "dt_rollover_end":'2001-01-01T00:00:00',
         "contract_subject":[
            {
               "id_service_type":'4',
               "id_municipal_resource":9,
               "dt_start_resource":'2012-04-27T00:00:00',
               "dt_end_resource":'2012-05-27T00:00:00',
               "nn_heating_system_form":0,
               "nn_heating_system_type":0
            }
         ],
        "address_object": [{
                            "id_fias_guid":id_fias_guid,
                    "house_object": []
                        }
                    ]

         })

    return(Json_setContract)

def generation_Account(id_fias_guid, id_house_object):
    Json_setAccount = setAccountJ(id_fias_guid, id_house_object)
    return (Json_setAccount)
def generation_MeteringDevice(id_fias_guid):
    Json_setMeteringDevice = setMeteringDeviceJ(id_fias_guid)
    return (Json_setMeteringDevice)
def generation_MeteringDV():
    Json_setMeteringDV = setMeteringDVJ()
    return (Json_setMeteringDV)
def generation_ChargeDocument():
    Json_setChargeDocument = setChargeDocumentJ()
    return (Json_setChargeDocument)
def generation_AddrObjData():
    Json_setAddrObjData = setAddrObjDataJ()
    return (Json_setAddrObjData)
def generation_HouseObjData(id_fias_guid):
    Json_setHouseObjData = setHouseObjDataJ(id_fias_guid)
    return (Json_setHouseObjData)
def generation_Payments():
    Json_setPayments = setPaymentsJ()
    return (Json_setPayments)
def generation_Contract(id_fias_guid):
    Json_setContract = setContractJ(id_fias_guid)
    return (Json_setContract)



