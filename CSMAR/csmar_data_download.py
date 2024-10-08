from csmarapi.CsmarService import CsmarService
csmar = CsmarService()
from csmarapi.ReportUtil import ReportUtil

# Decide the updated date
end_date = '2021-12-31'

# Chinese Version
csmar.login('gavin.feng@cityu.edu.hk','FengCityu2021','0')

# Download TRD_Nrrate
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('股票市场交易')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Nrrate')
ReportUtil(fields)
nrratelist = []
for i in range(len(fields)):
    nrratelist.append(fields[i]['field'])
csmar.getPackResultExt(nrratelist,'','TRD_Nrrate','',end_date)

# Download STK_MKT_THRFACDAY
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Fama-French因子')
ReportUtil(tables)
fields = csmar.getListFields('STK_MKT_THRFACDAY')
ReportUtil(fields)
stkmktlist = []
for i in range(len(fields)):
    stkmktlist.append(fields[i]['field'])
csmar.getPackResultExt(stkmktlist,'','STK_MKT_THRFACDAY','',end_date)

# English Version
csmar.login('gavin.feng@cityu.edu.hk','FengCityu2021')

# Download TRD_Co
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Co')
ReportUtil(fields)
colist = []
for i in range(len(fields)):
    colist.append(fields[i]['field'])
csmar.getPackResultExt(colist,'','TRD_Co','',end_date)

# Download TRD_Cndalym
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Cndalym')
ReportUtil(fields)
cndalymlist = []
for i in range(len(fields)):
    cndalymlist.append(fields[i]['field'])
csmar.getPackResultExt(cndalymlist,'','TRD_Cndalym','1990-01-01',end_date)

# Download TRD_Dalyr
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Dalyr')
ReportUtil(fields)
dalrylist = []
for i in range(len(fields)):
    dalrylist.append(fields[i]['field'])
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','2021-01-01',end_date)
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','2016-01-01','2020-12-31')
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','2011-01-01','2015-12-31')
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','2006-01-01','2010-12-31')
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','2001-01-01','2005-12-31')
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','1996-01-01','2000-12-31')
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','1991-01-01','1995-12-31')
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','1986-01-01','1990-12-31')
csmar.getPackResultExt(dalrylist,'','TRD_Dalyr','1981-01-01','1985-12-31')

# Download TRD_Mnth
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Mnth')
ReportUtil(fields)
mnthlist = []
for i in range(len(fields)):
    mnthlist.append(fields[i]['field'])
csmar.getPackResultExt(mnthlist,'','TRD_Mnth','',end_date)

# Download FS_Combas
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Financial Statements')
ReportUtil(tables)
fields = csmar.getListFields('FS_Combas')
ReportUtil(fields)
fscombaslist = []
for i in range(len(fields)):
    fscombaslist.append(fields[i]['field'])
csmar.getPackResultExt(fscombaslist,'','FS_Combas','',end_date)

# Download FS_Comins
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Financial Statements')
ReportUtil(tables)
fields = csmar.getListFields('FS_Comins')
ReportUtil(fields)
fscominslist = []
for i in range(len(fields)):
    fscominslist.append(fields[i]['field'])
csmar.getPackResultExt(fscominslist,'','FS_Comins','',end_date)

# Download FS_Comscfd
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Financial Statements')
ReportUtil(tables)
fields = csmar.getListFields('FS_Comscfd')
ReportUtil(fields)
fscomscfdlist = []
for i in range(len(fields)):
    fscomscfdlist.append(fields[i]['field'])
csmar.getPackResultExt(fscomscfdlist,'','FS_Comscfd','',end_date)

# Download FS_Comscfi
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Financial Statements')
ReportUtil(tables)
fields = csmar.getListFields('FS_Comscfi')
ReportUtil(fields)
fscomscfilist = []
for i in range(len(fields)):
    fscomscfilist.append(fields[i]['field'])
csmar.getPackResultExt(fscomscfilist,'','FS_Comscfi','',end_date)

# Download FN_Fn046
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Financial Statements')
ReportUtil(tables)
fields = csmar.getListFields('FN_Fn046')
ReportUtil(fields)
fnfn046list = []
for i in range(len(fields)):
    fnfn046list.append(fields[i]['field'])
csmar.getPackResultExt(fnfn046list,'','FN_Fn046','',end_date)

# Download CG_Co
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Corporate Governance')
ReportUtil(tables)
fields = csmar.getListFields('CG_Co')
ReportUtil(fields)
cgcolist = []
for i in range(len(fields)):
    cgcolist.append(fields[i]['field'])
csmar.getPackResultExt(cgcolist,'','CG_Co','',end_date)

# Download CD_Dividend
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Dividend Distribution')
ReportUtil(tables)
fields = csmar.getListFields('CD_Dividend')
ReportUtil(fields)
cddividendlist = []
for i in range(len(fields)):
    cddividendlist.append(fields[i]['field'])
csmar.getPackResultExt(cddividendlist,'','CD_Dividend','',end_date)

# Download TRD_Capchg
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Capchg')
ReportUtil(fields)
colist = []
for i in range(len(fields)):
    colist.append(fields[i]['field'])
csmar.getPackResultExt(colist,'','TRD_Capchg','',end_date)

# Download TRD_Index
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Index')
ReportUtil(fields)
colist = []
for i in range(len(fields)):
    colist.append(fields[i]['field'])
csmar.getPackResultExt(colist,'','TRD_Index','',end_date)

# Download TRD_Cnmont
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Cnmont')
ReportUtil(fields)
cndalymlist = []
for i in range(len(fields)):
    cndalymlist.append(fields[i]['field'])
csmar.getPackResultExt(cndalymlist,'','TRD_Cnmont','1990-01-01',end_date)

# Download TRD_Week
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Week')
ReportUtil(fields)
cndalymlist = []
for i in range(len(fields)):
    cndalymlist.append(fields[i]['field'])
csmar.getPackResultExt(cndalymlist,'','TRD_Week','1990-01-01',end_date)

# Download TRD_Weekcm
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Weekcm')
ReportUtil(fields)
cndalymlist = []
for i in range(len(fields)):
    cndalymlist.append(fields[i]['field'])
csmar.getPackResultExt(cndalymlist,'','TRD_Weekcm','1990-01-01',end_date)

# Download HLD_Contrshr
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Shareholder')
ReportUtil(tables)
fields = csmar.getListFields('HLD_Contrshr')
ReportUtil(fields)
cndalymlist = []
for i in range(len(fields)):
    cndalymlist.append(fields[i]['field'])
csmar.getPackResultExt(cndalymlist,'','HLD_Contrshr','1990-01-01',end_date)

# Download HLD_Shareholders
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Shareholder')
ReportUtil(tables)
fields = csmar.getListFields('HLD_Shareholders')
ReportUtil(fields)
cndalymlist = []
for i in range(len(fields)):
    cndalymlist.append(fields[i]['field'])
csmar.getPackResultExt(cndalymlist,'','HLD_Shareholders','1990-01-01',end_date)

# Download HLD_Negshr
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Shareholder')
ReportUtil(tables)
fields = csmar.getListFields('HLD_Negshr')
ReportUtil(fields)
cndalymlist = []
for i in range(len(fields)):
    cndalymlist.append(fields[i]['field'])
csmar.getPackResultExt(cndalymlist,'','HLD_Negshr','1990-01-01',end_date)

# Download TRD_Year
database = csmar.getListDbs()
ReportUtil(database)
tables = csmar.getListTables('Stock Trading')
ReportUtil(tables)
fields = csmar.getListFields('TRD_Year')
ReportUtil(fields)
mnthlist = []
for i in range(len(fields)):
    mnthlist.append(fields[i]['field'])
csmar.getPackResultExt(mnthlist,'','TRD_Year','',end_date)
