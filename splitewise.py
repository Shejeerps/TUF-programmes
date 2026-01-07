class splitewise:
    def solution(self):
        payment_summary={
            "hari":1200,
            "vipin":1400,
            "jhon":1000,
            "vishnu":0,
            "tom":120,
            "avinash":0,
            "jini":0,
            "ashok":0
        }

        total=sum(payment_summary.values())
        print(total)
        individual_split=total/len(payment_summary)
        print(individual_split)
        result={k:individual_split-v for k,v in payment_summary.items()}
        print(result)
sp=splitewise()
sp.solution()