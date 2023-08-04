from storipy.db import DB


class Account(DB):
    def insert(self, data):
        if isinstance(data, dict):
            data = [data]
        fields = "(%s, %s, %s)" % tuple(data[0].keys())
        values = [tuple(v.values()) for v in data]

        sql = f"INSERT INTO transaction {fields} VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE amount=amount"
        return self.create(sql, values)

    def credits(self) -> dict:
        sql = """SELECT CONCAT("$ ", FORMAT(AVG(amount),2)) credits FROM transaction WHERE amount > %s"""
        return self.one(sql, 0)

    def debits(self) -> dict:
        sql = """SELECT CONCAT("$ ", FORMAT(AVG(amount),2)) debits FROM transaction WHERE amount < %s"""
        return self.one(sql, 0)

    def balance(self):
        sql = """SELECT CONCAT("$ ", FORMAT(SUM(amount),2)) balance FROM transaction"""
        return self.one(sql)

    def month_activity(self):
        sql = """SELECT COUNT(*) count, MONTHNAME(created_at) month 
        FROM transaction GROUP BY MONTHNAME(created_at) 
        ORDER BY created_at"""

        return {"activity": self.all(sql)}

    def current_date(self):
        sql = """SELECT DATE_FORMAT(NOW(), "%b %e, %Y") date"""
        return self.one(sql)

    def recap(self, **kwargs) -> dict:
        return {
            **self.credits(),
            **self.debits(),
            **self.balance(),
            **self.current_date(),
            **self.month_activity(),
            **kwargs,
        }
