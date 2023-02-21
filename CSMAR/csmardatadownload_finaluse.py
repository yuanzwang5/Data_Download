
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
from csmarapi.CsmarService import CsmarService
csmar = CsmarService()
from csmarapi.ReportUtil import ReportUtil

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
