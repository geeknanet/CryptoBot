from tools import OrdersNotification


class OrderNotifier:
    def __init__(self, config, order):
        self.config = config
        self.order = order
        self.notifier = OrdersNotification(self.config)
        self.evaluator_notification = None

    def notify(self, evaluator_notification):
        self.evaluator_notification = evaluator_notification
        orders = [order for order in self.order.get_linked_orders()]
        orders.append(self.order)
        self.notifier.notify_create(evaluator_notification, orders, self.order.get_order_symbol())

    def end(self, order_filled, orders_canceled, trade_profitability, portfolio_profitability):
        self.notifier.notify_end(order_filled,
                                 orders_canceled,
                                 self.order.get_order_symbol(),
                                 trade_profitability,
                                 portfolio_profitability)
