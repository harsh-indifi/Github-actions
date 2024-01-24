APPLICATIONS_TABLE = """
applications"""

APPLICATIONS_TABLE_COLUMNS = {
    "id UUID PRIMARY KEY DEFAULT uuid_generate_v4()",
    '"requestId" SERIAL',
    "amount MONEY",
    "duration INTEGER"
}