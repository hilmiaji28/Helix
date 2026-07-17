from .base import AnalyticsService


class BusinessService(AnalyticsService):
    """
    Business KPI Engine
    """

    def total_customers(self):
        return self.df["Customer ID"].nunique()

    def total_transactions(self):
        return len(self.df)

    def total_revenue(self):
        return float(self.df["Total Amount"].sum())

    def average_order_value(self):
        return float(self.df["Total Amount"].mean())

    def average_rating(self):
        return float(self.df["Customer Rating"].mean())

    def returning_rate(self):
        return float(self.df["Is Returning Customer"].mean())

    def summary(self):
        return {
            "customers": self.total_customers(),
            "transactions": self.total_transactions(),
            "revenue": self.total_revenue(),
            "aov": self.average_order_value(),
            "rating": self.average_rating(),
            "returning_rate": self.returning_rate(),
        }
