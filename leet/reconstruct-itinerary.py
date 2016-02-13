class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        sorted_tickes = sorted(tickets)
        return find_order(sorted_tickes, 'JFK')


def find_order(tickets, src):
    # print tickets, src
    if len(tickets) == 1:
        return [tickets[0][0], tickets[0][1]]
    for i, el in enumerate(tickets):
        t_src, t_dest = el
        if t_src == src:
            rem_tickets = tickets[:i] + tickets[i+1:]
            order = find_order(rem_tickets, t_dest)
            # print order
            if len(order) > 0:
                return [src] + order
    return []


if __name__ == '__main__':
    sln = Solution()
    sln.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])