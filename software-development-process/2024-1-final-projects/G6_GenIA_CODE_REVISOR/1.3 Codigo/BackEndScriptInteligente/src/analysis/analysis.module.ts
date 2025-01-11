import { Module } from '@nestjs/common';
import { AnalysisService } from './analysis.service';
import { AnalysisController } from './analysis.controller';
import { PrismaModule } from '../../prisma/prisma.module';
import { OpenaiModule } from '../openai/openai.module';
import { PrismaService } from '../../prisma/prisma.service';

@Module({
  imports: [PrismaModule, OpenaiModule],
  providers: [AnalysisService, PrismaService],
  controllers: [AnalysisController],
})
export class AnalysisModule {}
