

#include <string>
#include <vector>

#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/param.h>
#include <sys/socket.h>
#include <sys/file.h>
#include <sys/time.h>

#include <netinet/in_systm.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
////#include <netinet/ip_var.h>
#include <netdb.h>
#include <unistd.h>
#include <stdio.h>
#include <ctype.h>
//#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <iostream>
#include<vector>
#include<ctime>
#include <unordered_map>
#include <algorithm>
#include <chrono>
#include <mutex>
#include <time.h>
#include <condition_variable>
#include "mls.h"

#define	DEFDATALEN	(ICMP_MINLEN)	/* default data length */
#define	MAXIPLEN	60
#define	MAXICMPLEN	76
#define	MAXPACKET	(65536 - 60 - ICMP_MINLEN)/* max packet size */


using std::chrono::steady_clock;

using namespace std;

struct point{
    timespec t;
    uint16_t indx;
};

namespace pinger
{
  class parPinger
  {
    public:
    parPinger(char* ip,  double ping_interval_sec, uint16_t threadID);
    ~parPinger();
    pthread_t probeRecverThread;
    pthread_t probeSenderThread;
    static void* recvMain(void * args);
    static void* sendMain(void * args);
    std::vector<point> send_times;
    double get_interval();

    std::vector<std::vector<long double>> curResult;
    std::vector<std::vector<long double>> probe();
    void set_ping_interval_sec(double value);
    void set_target_ip(char* ip, uint16_t threadID);

    private:
    long double ts2ld(struct timespec t);
    struct  timespec tsSubtract (struct  timespec  time1, struct  timespec  time2);
    string targetIP;
    uint16_t threadID;
    double burstTime;
    timespec ping_interval;
    int send_probe(string target_ip, vector<bool> mls_seq, uint16_t scanner_id);
    uint16_t in_cksum(uint16_t *addr, unsigned len);
    vector<bool> currPIR_MLS;
    long long pir_count;
    mls MLSgen;
    void timespec_diff(struct timespec &startOverhead, struct timespec &stopOverhead, struct timespec &sendInterval, struct timespec &computed_sleepInterval);
  };
}
