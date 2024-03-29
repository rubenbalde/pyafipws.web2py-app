# -*- coding: utf-8 -*-

migrate = True

db.define_table("pdftemplate",
    Field("title"),
    Field("format", requires=IS_IN_SET(["A4","legal","letter"])),
    migrate = migrate)

db.define_table("pdfelement",
    Field("pdftemplate", type=db.pdftemplate, represent = lambda id: db.pdftemplate[id].title),
    Field("name", requires=IS_NOT_EMPTY()),
    Field("type", length=2, requires=IS_IN_SET(['T', 'L', 'I', 'B', 'BC'])),
    Field("x1", "double", requires=IS_NOT_EMPTY()),
    Field("y1", "double", requires=IS_NOT_EMPTY()),
    Field("x2", "double", requires=IS_NOT_EMPTY()),
    Field("y2", "double", requires=IS_NOT_EMPTY()),
    Field("font", default="Arial", requires=IS_IN_SET(['Courier','Arial','Times','Symbol','Zapfdingbats'])),
    Field("size", "double", default="10", requires=IS_NOT_EMPTY()),
    Field("bold", "boolean"),
    Field("italic", "boolean"),
    Field("underline", "boolean"),
    Field("foreground", "integer", default=0x000000, comment="Color text"),
    Field("background", "integer", default=0xFFFFFF, comment="Fill color"),
    Field("align", "string", length=1, default="L", requires=IS_IN_SET(['L', 'R', 'C', 'J'])),
    Field("text", "text", comment="Default text"),
    Field("priority", "integer", default=0, comment="Z-Order"),
    migrate = migrate)
