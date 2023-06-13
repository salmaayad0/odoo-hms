{
    "name" : "HMS",
    "description" : "Hospitals Management System",
    "author" : "",
    "version" : "0.1",
    "depends" : ["base"],
    #data has all view => xml files 
    "data" : ['security/res_groups.xml',
              'security/ir.model.access.csv',
              'reports/report.xml',
              'reports/hms_patient_report.xml',
              'views/hms_patient.xml',
              'views/hms_deprtment.xml',
              'views/hms_doctor.xml',
              'views/hms_patient_id_inherit.xml'
              ]
}