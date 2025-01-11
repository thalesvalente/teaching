import { Module } from '@nestjs/common';
import { ScriptService } from './script.service';
import { ScriptController } from './scripts.controller';
import { PrismaModule } from '../../prisma/prisma.module';

@Module({
  imports: [PrismaModule],
  providers: [ScriptService],
  controllers: [ScriptController],
})
export class ScriptModule {}
