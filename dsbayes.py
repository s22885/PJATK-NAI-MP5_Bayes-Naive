class ArgsCont:
    dim: int
    argsArSet: list

    def __init__(self, dim: int):
        self.dim = dim
        self.argsArSet = [set() for zz in range(dim + 1)]

    def addArgOfPos(self, n: int, arg: str):
        self.argsArSet[n].add(arg)

    def addArgs(self, data_ar: list):
        for arg_pos in range(len(data_ar)):
            self.addArgOfPos(arg_pos, data_ar[arg_pos])

    def getSizeOfPos(self, n: int):
        return len(self.argsArSet[n])

    def getResList(self):
        return list(self.argsArSet[len(self.argsArSet) - 1])


class TrainCont:
    dim: int
    dataRecs: list
    allArgs: ArgsCont

    def __init__(self, dim: int):
        self.dim = dim
        self.dataRecs = []
        self.allArgs = ArgsCont(dim)

    def testList(self, data_arar):
        res = ""
        for data_ar in data_arar:
            res += str(data_ar) + " = " + str(self.test(data_ar)) + "\n"
        return res

    def test(self, data_ar):
        if len(data_ar) != self.dim:
            return
        # setup>
        res_list = self.allArgs.getResList()
        res_count = [0 for z in range(len(res_list))]
        argcnt_ar_ar = [[] for z in range(len(res_list))]
        for i in range(len(argcnt_ar_ar)):
            argcnt_ar_ar[i] = [0 for z in range(self.dim)]
        # <setup
        for rec_indv in self.dataRecs:
            res_type = rec_indv.getRes()
            r = -1
            for i in range(len(res_list)):
                if res_list[i] == res_type:
                    r = i
            res_count[r] += 1
            for i in range(len(data_ar)):
                if data_ar[i] == rec_indv.getArg(i):
                    argcnt_ar_ar[r][i] += 1
        for x in range(len(argcnt_ar_ar)):
            for y in range(len(argcnt_ar_ar[x])):
                if argcnt_ar_ar[x][y] == 0:
                    argcnt_ar_ar[x][y] = 1 / (res_count[x] + self.allArgs.getSizeOfPos(y))
                else:
                    argcnt_ar_ar[x][y] = argcnt_ar_ar[x][y] / res_count[x]
        for i in range(len(res_count)):
            res_count[i] = res_count[i] / len(self.dataRecs)
        prop = [val for val in res_count]
        for x in range(len(argcnt_ar_ar)):
            for y in range(len(argcnt_ar_ar[x])):
                prop[x] *= argcnt_ar_ar[x][y]
        k = -1
        size = -1
        for i in range(len(prop)):
            if prop[i] > size:
                size = prop[i]
                k = i
        return res_list[k]

    def addRecs(self, arg_arar: list):
        for arg_ar in arg_arar:
            self.addRec(arg_ar)

    def addRec(self, arg_ar: list):
        if len(arg_ar) != self.dim + 1:
            return
        self.allArgs.addArgs(arg_ar)
        tmp = RecordIndv(arg_ar)
        self.dataRecs.append(tmp)

    def getDim(self):
        return self.dim


class RecordIndv:
    args: list

    def __init__(self, arg_ar: list):
        self.args = arg_ar

    def getRes(self):
        return self.args[len(self.args) - 1]

    def getArg(self, n: int):
        return self.args[n]
