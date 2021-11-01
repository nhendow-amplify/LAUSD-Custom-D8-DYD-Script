import pandas as pd
import datetime


#read the dyd
dyd = pd.read_csv('/Users/jevans/Desktop/LAUSD Export/StudentSummary.csv')

#rename existing headers on left to values on right
dyd_renamed = dyd.rename(columns={                	'Enrollment Grade' : 'Grade' ,
                                                            	'Gender' : 'GENDER' ,
                                                              	'Race' : 'RACE' ,
                                                 	'Special Education' : 'SPECIAL_ED' ,
                                                        	'Disability' : 'DISABILITY' ,
                                               	'Specific Disability' : 'SPEC_DISAB' ,
                                                       	'Section 504' : 'SEC_504' ,
                                        	'Economically Disadvantaged' : 'ECON_DISADV' ,
                                                       	'Meal Status' : 'FREE_LUNCH' ,
                                                           	'Title 1' : 'TITLE_1' ,
                                                           	'Migrant' : 'MIGRANT' ,
                                               	'English Proficiency' : 'ENGPROF' ,
                                                        	'ELL Status' : 'ESL' ,
                                                     	'Home Language' : 'LANGUAGE' ,
                                              	'Alternate Assessment' : 'ALT_ASSMT' ,
                                           	'Approved Accommodations' : 'APPD_ACCOM' ,
                                                   	'Composite Level' : 'Assessment Measure-Composite Score-Levels' ,
                                                   	'Composite Score' : 'Assessment Measure-Composite Score-Score' ,
                                        	'Letter Names (LNF) - Level' : 'Assessment Measure-LNF-Levels' ,
                                        	'Letter Names (LNF) - Score' : 'Assessment Measure-LNF-Score' ,
                                  	'Phonemic Awareness (PSF) - Level' : 'Assessment Measure-PSF-Levels' ,
                                  	'Phonemic Awareness (PSF) - Score' : 'Assessment Measure-PSF-Score' ,
                                   	'Letter Sounds (NWF-CLS) - Level' : 'Assessment Measure-NWF (CLS)-Levels' ,
                                   	'Letter Sounds (NWF-CLS) - Score' : 'Assessment Measure-NWF (CLS)-Score' ,
                                        	'Decoding (NWF-WRC) - Level' : 'Assessment Measure-NWF (WRC)-Levels' ,
                                        	'Decoding (NWF-WRC) - Score' : 'Assessment Measure-NWF (WRC)-Score' ,
                                        	'Word Reading (WRF) - Level' : 'Assessment Measure-WRF-Levels' ,
                                        	'Word Reading (WRF) - Score' : 'Assessment Measure-WRF-Score' ,
                                     	'Reading Fluency (ORF) - Level' : 'Assessment Measure-ORF (Fluency)-Levels' ,
                                     	'Reading Fluency (ORF) - Score' : 'Assessment Measure-ORF (Fluency)-Score' ,
                               	'Reading Accuracy (ORF-Accu) - Level' : 'Assessment Measure-ORF (Accuracy)-Levels' ,
                               	'Reading Accuracy (ORF-Accu) - Score' : 'Assessment Measure-ORF (Accuracy)-Score' ,
                                          	'Error Rate (ORF) - Score' : 'Assessment Measure-ORF (Errors)-Score' ,
                              	'Reading Comprehension (Maze) - Level' : 'Assessment Measure-Maze-Levels' ,
                              	'Reading Comprehension (Maze) - Score' : 'Assessment Measure-Maze-Score' ,
                                  	'Correct Responses (Maze) - Score' : 'Assessment Measure-Maze (Correct)-Score' ,
                                	'Incorrect Responses (Maze) - Score' : 'Assessment Measure-Maze (Incorrect)-Score' ,
                                             	'Student ID (State ID)' : 'ELD_Level' })

#insert columns and data
dyd_renamed.insert(0, 'Roster Option', 'On Test Day')
dyd_renamed.insert(0, 'RF School', 'N')

    
#change "At Benchmark" to "Benchmark".  this may not be required later if the RAS team fixes the source
dyd_renamed.replace("At Benchmark", "Benchmark", inplace = True)

#convert date formats
dyd_renamed['Enrollment Date'] = pd.to_datetime(dyd_renamed['Enrollment Date'])
dyd_renamed['Date of Birth'] = pd.to_datetime(dyd_renamed['Date of Birth'])
dyd_renamed['Client Date'] = pd.to_datetime(dyd_renamed['Client Date'])
dyd_renamed['Sync Date'] = pd.to_datetime(dyd_renamed['Sync Date'])

#final selection of columns in order
dyd_final = dyd_renamed[[
	'School Year' ,
	'Roster Option' ,
	'External Program' ,
	'State' ,
	'Account Name' ,
	'Municipality Name' ,
	'Municipality Primary ID' ,
	'District Name' ,
	'District Primary ID' ,
	'Internal Program' ,
	'School Name' ,
	'Primary School ID' ,
	'Secondary School ID' ,
	'RF School' ,
	'Student Last Name' ,
	'Student First Name' ,
	'Student Middle Name' ,
	'Enrollment Date' ,
	'Grade' ,
	'Date of Birth' ,
	'GENDER' ,
	'RACE' ,
	'SPECIAL_ED' ,
	'DISABILITY' ,
	'SPEC_DISAB' ,
	'SEC_504' ,
	'ECON_DISADV' ,
	'FREE_LUNCH' ,
	'TITLE_1' ,
	'MIGRANT' ,
	'ENGPROF' ,
	'ESL' ,
	'LANGUAGE' ,
	'ALT_ASSMT' ,
	'APPD_ACCOM' ,
	'Classed' ,
	'Reporting Class Name' ,
	'Reporting Class ID' ,
	'Official Teacher Name' ,
	'Official Teacher Staff ID' ,
	'Assessing Teacher Name' ,
	'Assessing Teacher Staff ID' ,
	'Assessment' ,
	'Assessment Edition' ,
	'Assessment Grade' ,
	'Benchmark Period' ,
	'Assessment Measure-Composite Score-Levels' ,
	'Assessment Measure-Composite Score-Score' ,
	'Assessment Measure-LNF-Levels' ,
	'Assessment Measure-LNF-Score' ,
	'Assessment Measure-PSF-Levels' ,
	'Assessment Measure-PSF-Score' ,
	'Assessment Measure-NWF (CLS)-Levels' ,
	'Assessment Measure-NWF (CLS)-Score' ,
	'Assessment Measure-NWF (WRC)-Levels' ,
	'Assessment Measure-NWF (WRC)-Score' ,
	'Assessment Measure-WRF-Levels' ,
	'Assessment Measure-WRF-Score' ,
	'Assessment Measure-ORF (Fluency)-Levels' ,
	'Assessment Measure-ORF (Fluency)-Score' ,
	'Assessment Measure-ORF (Accuracy)-Levels' ,
	'Assessment Measure-ORF (Accuracy)-Score' ,
	'Assessment Measure-ORF (Errors)-Score' ,
	'Assessment Measure-Maze-Levels' ,
	'Assessment Measure-Maze-Score' ,
	'Assessment Measure-Maze (Correct)-Score' ,
	'Assessment Measure-Maze (Incorrect)-Score' ,
	'Client Date' ,
	'Sync Date' ,
	'Student Primary ID' ,
	'Primary ID - Student ID (School ID)' ,
	'ELD_Level'
]]

#set the date for the file name
x = datetime.datetime.now()

#write changes to csv
dyd_final.to_csv(('/Users/jevans/Desktop/LAUSD Export/LAUSD_D8_DYD_' + x.strftime("%m%d%y") + '.csv'), index=False, line_terminator = '\r\n')

print("Initial row count not including header:" + str(len(dyd.index)))
print("Final row count not including header:" + str(len(dyd_final.index)))

