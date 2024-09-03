# mf4_data_validation
Validate .mf4 data before and after merging

工作上遇到一个奇怪的要求：客户要求我们合并几个.mf4文件并将合并前后的数据进行对比，检查是否一致。以前没想过这个问题，这次便记录一下。

## 前提

由于连续测量的数据，timestamp什么的并无重合的部分。

使用Python包asammdf进行的合并。

## 结论

前后timestamp数量都不一致，数据肯定不一样。Matlab也可复现这个结果。除非我对mf4的编码方式理解有误。

可见asammdf的合并并不靠谱。