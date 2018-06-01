#include <stdio.h>
#include <stdlib.h>
#include "lz4f_toplevel.h"

//#define BUF_SIZE (16*1024)
//#define LZ4_HEADER_SIZE 19
#define LZ4_FOOTER_SIZE 4
//

//static const LZ4F_frameInfo_t lz4_frameInfo = {
//
//}

//void init_prefs(LZ4F_preferences_t *prefs, LZ4F_frameInfo_t *frameInfo){
//    memset(prefs, 0, sizeof(*prefs));
//
//    frameInfo->blockSizeID = LZ4F_default;
//    frameInfo->blockMode = LZ4F_blockLinked;
//    frameInfo->contentChecksumFlag = LZ4F_noContentChecksum;
//    frameInfo->frameType = LZ4F_frame;
//    frameInfo->contentSize = 0;
//    frameInfo-> = ;
//
//
//
//    LZ4F_frameInfo_t frameInfo = {
//        LZ4F_default,           // blockSizeID
//                                // The larger the block size, the (slightly) better the compression ratio)
//                                // Larger blocks also increase memory usage on both compression and decompression sides
//                                // Values: LZ4F_default, LZ4F_max64KB, LZ4F_max256KB, LZ4F_max1MB, LZ4F_max4MB
//
//        LZ4F_blockLinked,       // blockMode
//                                // Linked blocks sharply reduce inefficiencies when using small blocks,
//                                // they compress better. Some LZ4 decoders are only compatible with independent blocks.
//                                // Values: LZ4F_blockLinked, LZ4F_blockIndependent
//
//        LZ4F_noContentChecksum, // contentChecksumFlag
//                                // Values: LZ4F_noContentChecksum, LZ4F_contentChecksumEnabled
//
//        LZ4F_frame,             // frameType
//                                // Values: LZ4F_frame, LZ4F_skippableFrame
//
//        0,                      // contentSize (0 for unknown)
//        0,                      // dictID (0 == no dictID provided)
//
//        LZ4F_noBlockChecksum,   // blockChecksumFlag
//                                // Values: LZ4F_noBlockChecksum, LZ4F_blockChecksumEnabled
//    };
//
//    LZ4F_preferences_t prefs = {
//        frameInfo,
//        0,              // compressionLevel (0 == default (fast mode))
//                        // values > LZ4HC_CLEVEL_MAX count as LZ4HC_CLEVEL_MAX; values < 0 trigger "fast acceleration"
//        1,              // autoFlush, 1 == always flush
//        {0, 0, 0, 0}    // reserved (must be zero for forward compatibility)
//    };
//}

char* LZ4F_compressFrame_default(size_t pyHeaderLen, const char* srcBuffer, size_t srcSize, size_t* compressed_size){
    size_t destination_size;

    LZ4F_frameInfo_t frameInfo = {
        LZ4F_default,           // blockSizeID
                                // The larger the block size, the (slightly) better the compression ratio)
                                // Larger blocks also increase memory usage on both compression and decompression sides
                                // Values: LZ4F_default, LZ4F_max64KB, LZ4F_max256KB, LZ4F_max1MB, LZ4F_max4MB

        LZ4F_blockLinked,       // blockMode
                                // Linked blocks sharply reduce inefficiencies when using small blocks,
                                // they compress better. Some LZ4 decoders are only compatible with independent blocks.
                                // Values: LZ4F_blockLinked, LZ4F_blockIndependent

        LZ4F_noContentChecksum, // contentChecksumFlag
                                // Values: LZ4F_noContentChecksum, LZ4F_contentChecksumEnabled

        LZ4F_frame,             // frameType
                                // Values: LZ4F_frame, LZ4F_skippableFrame

        srcSize,                      // contentSize (0 for unknown)
        0,                      // dictID (0 == no dictID provided)

        LZ4F_noBlockChecksum   // blockChecksumFlag
                                // Values: LZ4F_noBlockChecksum, LZ4F_blockChecksumEnabled
    };

    LZ4F_preferences_t prefs = {
        frameInfo,
        0,              // compressionLevel (0 == default (fast mode))
                        // values > LZ4HC_CLEVEL_MAX count as LZ4HC_CLEVEL_MAX; values < 0 trigger "fast acceleration"
        1,              // autoFlush, 1 == always flush
        {0, 0, 0, 0}    // reserved (must be zero for forward compatibility)
    };

    if(!srcSize){
        *compressed_size = 0;
        return NULL;
    }

    //initialize_prefs(&prefs, &frameInfo);

    destination_size = LZ4F_compressFrameBound (srcSize, &prefs) + LZ4F_HEADER_SIZE_MAX + LZ4_FOOTER_SIZE;
    char* dstBuffer = (char *)malloc(destination_size + pyHeaderLen);
    if (!dstBuffer) {
		printf("Not enough memory");
		return NULL;
	}

	*compressed_size = LZ4F_compressFrame (dstBuffer + pyHeaderLen, destination_size, srcBuffer, srcSize, &prefs);
    if (LZ4F_isError (*compressed_size))
    {
        free(dstBuffer);
        printf("LZ4F_compressFrame failed with code: %s", LZ4F_getErrorName (*compressed_size));
        *compressed_size = 0;
        return NULL;
    }

    return dstBuffer;
}

